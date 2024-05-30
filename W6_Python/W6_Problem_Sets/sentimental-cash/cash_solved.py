def main():
    # Get the total amount in cents from user input
    amount = get_cents()
    
    # Calculate the number of each type of coin
    coins = {
        'quarters': amount // 25,
        'dimes': (amount % 25) // 10,
        'nickels': ((amount % 25) % 10) // 5,
        'pennies': ((amount % 25) % 10) % 5
    }
    
    # Sum the total number of coins
    total_coins = sum(coins.values())
    
    # Print the total number of coins
    print(total_coins)


def get_cents():
    while True:
        try:
            # Prompt user for input and convert to float
            amount = float(input("Input Change: "))
            
            # Ensure the amount is non-negative
            if amount >= 0:
                return int(amount * 100)  # Convert dollars to cents
            else:
                print("Please enter a non-negative amount.")
        except ValueError:
            print("Please enter a valid number.")


# Entry point of the program
main()