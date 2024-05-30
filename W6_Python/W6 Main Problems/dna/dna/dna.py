import csv
import sys

def main():
    # Check for command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        sys.exit(1)

    # Paths to the database and sequence files from command-line arguments
    db_path = sys.argv[1]
    seq_path = sys.argv[2]

    # Load the database from the CSV file
    people = []  # Renamed from 'database' to 'people' for clarity
    with open(db_path) as file:
        reader = csv.DictReader(file)
        for person in reader:  # Renamed from 'row' to 'person' for clarity
            people.append(person)

    # Load the DNA sequence from the file
    with open(seq_path) as file:
        dna = file.read().strip()  # Renamed from 'sequence' to 'dna'

    # Find the longest match of each STR in the DNA sequence
    str_matches = {str: longest_match(dna, str) for str in people[0] if str != "name"}

    # Look for a matching profile in the database
    for person in people:  # Renamed 'profile' to 'person' for consistency
        if all(int(person[str]) == match for str, match in str_matches.items()):
            print(person["name"])
            return

    print("No match")

def longest_match(dna, str):
    """Finds the longest sequence of repeated STRs in the DNA sequence."""

    # Variables to track the longest sequence found
    max_length = 0  # Renamed from 'longest_run' for clarity
    str_len = len(str)  # Renamed for clarity
    dna_len = len(dna)  # Renamed for clarity

    # Search the DNA sequence for STR repeats
    for i in range(dna_len):
        count = 0  # Tracks consecutive STR repeats

        while True:
            start = i + count * str_len
            end = start + str_len

            if dna[start:end] == str:
                count += 1
            else:
                break

        max_length = max(max_length, count)

    return max_length

main()
