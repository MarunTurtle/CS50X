while True:
    try:
        n = int(input("Number: "))
        if n >= 1 and 8 >= n:
            break
        else:
            print("Please enter a number between 1 and 8.")
    except ValueError:
        print("Please enter a valid number.")

for i in range(n):
    spaces = " " * (n - i - 1)
    hashes = "#" * (i + 1)
    print(spaces + hashes + "  " + hashes)
