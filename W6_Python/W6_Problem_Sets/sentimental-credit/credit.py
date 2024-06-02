import re

def main():
    # Prompt user for card number until a valid input is received
    while True:
        try:
            card_number = input("Number: ")
            if re.match(r"^\d+$", card_number):  # Ensure input is digits only
                n = int(card_number)
                if n >= 0:
                    break
                else:
                    print("Please enter a non-negative number.")
            else:
                print("Please enter a valid number.")
        except ValueError:
            print("Please enter a valid number.")

    # Determine the length of the card number
    card_length = len(card_number)

    # Validate card length
    if card_length not in [13, 15, 16]:
        print("INVALID")
        return

    # Calculate checksum using Luhn's Algorithm
    total = 0
    for i in range(card_length):
        digit = int(card_number[i])
        if i % 2 == card_length % 2:  # Double every second digit from the right
            digit *= 2
            if digit > 9:  # Subtract 9 from numbers greater than 9
                digit -= 9
        total += digit

    # Validate checksum
    if total % 10 != 0:
        print("INVALID")
        return

    # Determine card type based on starting digits and length
    start = int(card_number[:2])
    if card_length == 16 and 51 <= start <= 55:
        print("MASTERCARD")
    elif card_length == 15 and (start == 34 or start == 37):
        print("AMEX")
    elif (card_length == 13 or card_length == 16) and card_number[0] == '4':
        print("VISA")
    else:
        print("INVALID")

if __name__ == "__main__":
    main()