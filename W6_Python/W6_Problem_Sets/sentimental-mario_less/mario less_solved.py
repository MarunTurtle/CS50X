# Loop until a valid number between 1 and 8 is entered
while True:
    try:
        n = int(input("Number: "))  # Prompt user for a number
        if 1 <= n <= 8:  # Check if the number is within the valid range
            break  # Exit loop if valid number is entered
        else:
            print("Please enter a number between 1 and 8.")  # Prompt for correct range
    except ValueError:
        print("Please enter a valid number.")  # Handle non-integer input

# Generate the pyramid pattern
for i in range(n):
    # Print leading spaces
    for j in range(n - i - 1):
        print(" ", end="")
    # Print hashes
    for k in range(i + 1):
        print("#", end="")
    print()  # Move to the next line after each row