# Import necessary modules
import re


def lcount(text):
    # Use list comprehension and isalpha() to count letters
    return sum(1 for char in text if char.isalpha())


def wcount(text):
    # Split the text by spaces and count the words
    return len(text.split())


def scount(text):
    # Use re.findall to count '.', '!', and '?'
    return len(re.findall(r'[.!?]', text))


def main():
    # Prompt the user for some text
    text = input("Text: \n")

    # Count letters, words, and sentences
    letters = lcount(text)
    words = wcount(text)
    sentences = scount(text)

    # Calculate L and S for the Coleman-Liau index
    L = (letters / words) * 100
    S = (sentences / words) * 100

    # Calculate the index
    result = 0.0588 * L - 0.296 * S - 15.8

    # Determine and print the grade level
    if result < 1:
        print("Before Grade 1")
    elif result >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {round(result)}")


# Call the main function
if __name__ == "__main__":
    main()
