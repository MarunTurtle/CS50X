import re


def main():
    # Get card number
    while True:
        try:
            card_number = input("Number: ")
            if re.match(r"^\d+$", card_number):  # Check if input consists of digits only
                n = int(card_number)
                if n >= 0:
                    break
                else:
                    print("Please enter a non-negative number.")
            else:
                print("Please enter a valid number.")
        except ValueError:
            print("Please enter a valid number.")

    # Count length
    card_length = len(card_number)

    # Check if length is valid
    if card_length not in [13, 15, 16]:
        print("INVALID")
        return

    # Calculate checksum
    total = 0
    for i in range(card_length):
        digit = int(card_number[i])
        if i % 2 == card_length % 2:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit

    # Next check Luhn Algorithm
    if total % 10 != 0:
        print("INVALID")
        return

    # Get starting digits
    start = int(card_number[:2])

    # Next check starting digits for card type
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
