def main():
    amount = get_cents()
    coins = {
        'quarters': amount // 25,
        'dimes': (amount % 25) // 10,
        'nickels': ((amount % 25) % 10) // 5,
        'pennies': ((amount % 25) % 10) % 5
    }
    total_coins = sum(coins.values())
    print(total_coins)


def get_cents():
    while True:
        try:
            amount = float(input("Input Change: "))
            if amount >= 0:
                return int(amount * 100)  # Convert dollars to cents
            else:
                print("Please enter a non-negative amount.")
        except ValueError:
            print("Please enter a valid number.")


main()
