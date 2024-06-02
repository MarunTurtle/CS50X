import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter for currency formatting
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # Clear any existing user session
    session.clear()

    # Handle form submission
    if request.method == "POST":
        # Validate form inputs
        if not request.form.get("username"):
            return apology("must insert username", 400)
        elif not request.form.get("password"):
            return apology("must insert password", 400)
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("passwords do not match", 400)

        # Check if username already exists
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))
        if len(rows) != 0:
            return apology("username already exists", 400)

        # Insert new user into database
        db.execute("INSERT INTO users (username, hash) VALUES(?, ?)",
                   request.form.get("username"), generate_password_hash(request.form.get("password")))

        # Retrieve the id of the new user
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))
        if len(rows) != 1:
            return apology("error in retrieving new user id", 400)

        # Log in the new user
        session["user_id"] = rows[0]["id"]

        return redirect("/")

    # Render registration form
    else:
        return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""
    # Clear any existing user session
    session.clear()

    # Handle form submission
    if request.method == "POST":
        # Validate form inputs
        if not request.form.get("username"):
            return apology("must provide username", 403)
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Validate username and password
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Log in the user
        session["user_id"] = rows[0]["id"]

        return redirect("/")

    # Render login form
    else:
        return render_template("login.html")

@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        quote = lookup(symbol)
        if not quote:
            return apology("invalid symbol", 400)
        return render_template("quote.html", quote=quote)
    else:
        return render_template("quote.html")

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol").upper()
        shares = request.form.get("shares")
        # Validate form inputs
        if not symbol:
            return apology("must insert symbol")
        elif not shares or not shares.isdigit() or int(shares) <= 0:
            return apology("must insert a positive integer number")

        # Lookup stock price
        quote = lookup(symbol)
        if quote is None:
            return apology("no such symbol exists")

        price = quote["price"]
        total_cost = int(shares) * price
        cash = db.execute("SELECT cash FROM users WHERE id = :user_id",
                          user_id=session["user_id"])[0]["cash"]

        # Check if user has enough cash
        if cash < total_cost:
            return apology("not enough cash")

        # Update user's cash and record transaction
        db.execute("UPDATE users SET cash = cash - :total_cost WHERE id = :user_id",
                   total_cost=total_cost, user_id=session["user_id"])
        db.execute("INSERT INTO transactions (user_id, symbol, shares, price) VALUES (:user_id, :symbol, :shares, :price)",
                   user_id=session["user_id"], symbol=symbol, shares=shares, price=price)

        flash(f"Successfully purchased {shares} shares of {symbol} for {usd(total_cost)}.")
        return redirect("/")

    else:
        return render_template("buy.html")

@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    # Query for user's stocks and cash
    stocks = db.execute("SELECT symbol, SUM(shares) as total_shares FROM transactions WHERE user_id = :user_id GROUP BY symbol HAVING total_shares > 0",
                        user_id=session["user_id"])
    cash = db.execute("SELECT cash FROM users WHERE id = :user_id",
                      user_id=session["user_id"])[0]["cash"]

    total_value = cash
    grand_total = cash

    # Calculate total value of stocks
    for stock in stocks:
        quote = lookup(stock["symbol"])
        stock["price"] = quote["price"]
        stock["value"] = quote["price"] * stock["total_shares"]
        total_value += stock["value"]
        grand_total += stock["value"]

    return render_template("index.html", stocks=stocks, cash=cash, total_value=total_value, grand_total=grand_total)

@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    # Get user's stocks
    stocks = db.execute("SELECT symbol, SUM(shares) as total_shares FROM transactions WHERE user_id = :user_id GROUP BY symbol HAVING total_shares > 0",
                        user_id=session["user_id"])

    # Handle form submission
    if request.method == "POST":
        symbol = request.form.get("symbol").upper()
        shares = request.form.get("shares")

        # Validate form inputs
        if not symbol:
            return apology("must provide symbol")
        elif not shares or not shares.isdigit() or int(shares) <= 0:
            return apology("must provide a positive integer number of shares")
        else:
            shares = int(shares)
            for stock in stocks:
                if stock["symbol"] == symbol:
                    if stock["total_shares"] < shares:
                        return apology("not enough shares")
                    else:
                        # Get quote
                        quote = lookup(symbol)
                        if quote is None:
                            return apology("symbol not found")
                        price = quote["price"]
                        total_sale = shares * price

                        # Update user's cash and record transaction
                        db.execute("UPDATE users SET cash = cash + :total_sale WHERE id = :user_id",
                                   total_sale=total_sale, user_id=session["user_id"])
                        db.execute("INSERT INTO transactions (user_id, symbol, shares, price) VALUES (:user_id, :symbol, :shares, :price)",
                                   user_id=session["user_id"], symbol=symbol, shares=-shares, price=price)

                        flash(f"Successfully sold {shares} shares of {symbol} for {usd(total_sale)}!")
                        return redirect("/")

        return apology("symbol not found")

    # Render sell form
    else:
        return render_template("sell.html", stocks=stocks)

@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    # Query database for user's transactions, ordered by most recent first
    transactions = db.execute(
        "SELECT * FROM transactions WHERE user_id = :user_id ORDER BY timestamp DESC", user_id=session["user_id"]
    )
    # Render history page with transactions
    return render_template("history.html", transactions=transactions)

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/logout")
def logout():
    """Log user out"""
    # Clear any existing user session
    session.clear()
    # Redirect user to login form
    return redirect("/")

@app.route("/change_password", methods=["GET", "POST"])
@login_required
def change_password():
    """Allow user to change password"""
    if request.method == "POST":
        # Get form data
        current_password = request.form.get("current_password")
        new_password = request.form.get("new_password")
        confirm_password = request.form.get("confirm_password")

        # Validate form inputs
        if not current_password or not new_password or not confirm_password:
            return apology("must provide all fields")
        if new_password != confirm_password:
            return apology("new passwords do not match")

        # Query database for user's current password hash
        user_id = session["user_id"]
        user = db.execute("SELECT * FROM users WHERE id = :user_id", user_id=user_id)
        if len(user) != 1 or not check_password_hash(user[0]["hash"], current_password):
            return apology("invalid current password")

        # Update password hash in the database
        new_hash = generate_password_hash(new_password)
        db.execute("UPDATE users SET hash = :new_hash WHERE id = :user_id",
                   new_hash=new_hash, user_id=user_id)

        flash("Password changed successfully")
        return redirect("/")

    return render_template("change_password.html")