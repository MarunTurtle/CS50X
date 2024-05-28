text = "In the great green room"

# Round 1
print("Round 1")
for word in text.split():
    print(word)
print()

# Round 2
print("Round 2")
for word in text.split():
    for c in word:
        print(c)
print()

# Round 3
print("Round 3")
for word in text.split():
    if "g" in word:
        print(word)
print()

# Round 4
print("Round 4")
for word in text.split()[2:]:
    print(word)
print()

# Round 5
print("Round 5")
for word in text.split():
    print("Goodnight Moon")
print()
