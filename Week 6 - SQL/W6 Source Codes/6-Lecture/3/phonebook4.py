# Implements a phone book using a dictionary

people = {
    "Carter": "+1-617-495-1000",
    "David": "+1-617-495-1000",
    "John": "+1-949-468-2750",
}

# Search for name
name = input("Name: ")

if name in people:
    print(f"Number: {people[name]}")
else:
    print("Not found")
