# Loop until a valid number between 1 and 8 is entered
while True:
    try:
        n = int(input("Number: "))  # Prompt user for a number
        if 1 <= n <= 8:  # Check if the number is within the valid range
            break  # Exit loop if valid number is entered
        else:
            print("Please enter a number between 1 and 8.")  # Prompt user to enter a valid number
    except ValueError:
        print("Please enter a valid number.")  # Handle non-integer input

# Generate and print the pyramid pattern
for i in range(n):
    spaces = " " * (n - i - 1)  # Calculate leading spaces
    hashes = "#" * (i + 1)  # Calculate hashes for the current level
    print(spaces + hashes + "  " + hashes)  # Print the current level of the pyramid