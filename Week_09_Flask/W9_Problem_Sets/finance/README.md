# C$50 Finance

[CS50 Finance Problem Set](https://cs50.harvard.edu/x/2024/psets/9/finance/)

## Project Overview

C$50 Finance is a web application designed to help users manage their stock portfolios and record transactions. Built using the Flask framework, the application offers a user-friendly interface for stock trading and portfolio management.

## Project Features

- **User Authentication:** Secure registration, login, and password change functionalities.
- **Portfolio Management:** View stock holdings and portfolio value.
- **Stock Trading:** Buy and sell stocks.
- **Stock Quotes:** Retrieve current stock prices.
- **Transaction History:** View transaction history.

## Project Files

- **`app.py`:** Main script that runs the Flask application, handles routing, and implements core functionality.
- **`templates/`:** Directory containing HTML templates for different pages.
  - **`buy.html`:** Page for buying stocks.
  - **`history.html`:** Page for viewing transaction history.
  - **`index.html`:** Portfolio dashboard page.
  - **`layout.html`:** Base layout template.
  - **`change_password.html`:** Page for changing the password.
  - **`login.html`:** Login page.
  - **`register.html`:** Registration page.
  - **`sell.html`:** Page for selling stocks.
  - **`quote.html`:** Page for getting stock quotes.

## Detailed Description

### Flask Setup

The application is built using the Flask framework. The main routing and functionality are implemented in `app.py`, while HTML templates are used to render different pages.

### Template Inheritance

The `layout.html` file serves as the base layout, which other HTML templates extend. This ensures a consistent look and feel across all pages.

### Stock Trading

The `buy.html` and `sell.html` pages allow users to buy and sell stocks, respectively. Users input the stock symbol and the number of shares they want to trade.

### Portfolio and Transaction History

The `index.html` page displays the user's stock portfolio, including the total value. The `history.html` page shows a detailed transaction history, including the type of transaction, stock symbol, number of shares, price, total value, and date.

### Stock Quotes

The `quote.html` page allows users to input a stock symbol and retrieve the current stock price.

### User Authentication

Users can register on the `register.html` page, log in on the `login.html` page, and change their password on the `change_password.html` page.

## Code Design

- **Language:** Python and Flask for backend logic, HTML, and CSS for frontend design.
- **Modular Structure:** Each feature is implemented in a separate HTML file, and Flask routing connects these pages.
- **Database:** SQLite or any other relational database can be used to store user information and transaction history.

## Future Improvements

- **Enhanced User Interface:** Improve the UI for a better user experience and implement responsive design.
- **Additional Features:** Add stock alert settings, portfolio analysis tools, etc.
- **Security Enhancements:** Strengthen security measures to protect user data.