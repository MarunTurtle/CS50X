import re

def lcount(text):
    # Count the number of alphabetic characters in the text
    return sum(1 for char in text if char.isalpha())

def wcount(text):
    # Count the number of words in the text by splitting on spaces
    return len(text.split())

def scount(text):
    # Count the number of sentences by finding '.', '!', and '?'
    return len(re.findall(r'[.!?]', text))

def main():
    # Prompt the user for input text
    text = input("Text: \n")

    # Count letters, words, and sentences in the input text
    letters = lcount(text)
    words = wcount(text)
    sentences = scount(text)

    # Calculate L (average number of letters per 100 words)
    L = (letters / words) * 100
    # Calculate S (average number of sentences per 100 words)
    S = (sentences / words) * 100

    # Calculate the Coleman-Liau index
    result = 0.0588 * L - 0.296 * S - 15.8

    # Determine and print the grade level based on the index
    if result < 1:
        print("Before Grade 1")
    elif result >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {round(result)}")

# Execute the main function if the script is run directly
if __name__ == "__main__":
    main()