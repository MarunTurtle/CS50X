#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int lcount(string text);
int wcount(string text);
int scount(string text);

int main(void)
{
    // Prompt the user for some text
    string text = get_string("Text: \n");

    // int lcount = count letters
    int letters = lcount(text);

    // int wcount = count words
    int words = wcount(text);

    // int scount = count sentences
    int sentences = scount(text);

    // Coleman Liau Function

    // L = average number of letters per 100 words
    float L = ((float) letters / words) * 100.0;

    // S = average number of sentences per 100 words
    float S = ((float) sentences / words) * 100.0;

    // index = 0.0588 * L - 0.296 * S - 15.8
    float result = (0.0588 * L) - (0.296 * S) - 15.8;

    // Print the Grade Level
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

int lcount(string text)
{

    int n = strlen(text);
    int x = 0;

    for (int i = 0; i < n; i++)
    {
        if (isalpha(text[i]))
        {
            x += 1;
        }
    }

    return x;
}

int scount(string text)
{

    int n = strlen(text);
    int x = 0;

    for (int i = 0; i < n; i++)
    {
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            x += 1;
        }
    }

    return x;
}

int wcount(string text)
{

    int n = strlen(text);
    int x = 1;

    for (int i = 0; i < n; i++)
    {
        if (isspace(text[i]))
        {
            x += 1;
        }
    }

    return x;
}
