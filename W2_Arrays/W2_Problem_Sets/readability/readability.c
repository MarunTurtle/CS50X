#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

// Function prototypes
int lcount(string text);
int wcount(string text);
int scount(string text);

int main(void)
{
    // Prompt the user for some text
    string text = get_string("Text: \n");

    // Count letters, words, and sentences in the text
    int letters = lcount(text);
    int words = wcount(text);
    int sentences = scount(text);

    // Calculate the average number of letters and sentences per 100 words
    float L = ((float) letters / words) * 100.0;
    float S = ((float) sentences / words) * 100.0;

    // Calculate the Coleman-Liau index
    float result = (0.0588 * L) - (0.296 * S) - 15.8;

    // Print the Grade Level based on the index
    if (result < 0)
    {
        printf("Before Grade 1\n");
    }
    else if (result >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %.0f\n", result);
    }
}

// Function to count the number of letters in the text
int lcount(string text)
{
    int n = strlen(text);
    int x = 0;

    // Iterate through each character and count letters
    for (int i = 0; i < n; i++)
    {
        if (isalpha(text[i]))
        {
            x += 1;
        }
    }

    return x;
}

// Function to count the number of sentences in the text
int scount(string text)
{
    int n = strlen(text);
    int x = 0;

    // Iterate through each character and count sentence-ending punctuation
    for (int i = 0; i < n; i++)
    {
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            x += 1;
        }
    }

    return x;
}

// Function to count the number of words in the text
int wcount(string text)
{
    int n = strlen(text);
    int x = 1; // Start with 1 to account for the first word

    // Iterate through each character and count spaces
    for (int i = 0; i < n; i++)
    {
        if (isspace(text[i]))
        {
            x += 1;
        }
    }

    return x;
}