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
    for j in range(n - i - 1):
        print(" ", end="")
    for k in range(i + 1):
        print("#", end="")
    print()
