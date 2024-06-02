#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Function prototype for rotating a character by a given key
char rotate(char c, int key);

int main(int argc, string argv[])
{
    // Ensure exactly one command-line argument is provided
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    // Validate that the command-line argument is a digit
    for (int i = 0, n = strlen(argv[1]); i < n; i++)
    {
        if (!isdigit(argv[1][i]))
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }

    // Convert the command-line argument to an integer key
    int key = atoi(argv[1]);

    // Prompt user for plaintext input
    string plaintext = get_string("plaintext: ");

    // Print the ciphertext header
    printf("ciphertext: ");

    // Encrypt each character in the plaintext
    for (int i = 0, n = strlen(plaintext); i < n; i++)
    {
        char cipher_char = rotate(plaintext[i], key);
        printf("%c", cipher_char);
    }

    // Print a newline after the ciphertext
    printf("\n");

    return 0;
}

// Rotate a character by the given key using the Caesar cipher
char rotate(char c, int key)
{
    if (isalpha(c))
    {
        // Determine the base character ('A' for uppercase, 'a' for lowercase)
        char base = isupper(c) ? 'A' : 'a';
        
        // Apply the Caesar cipher formula and return the rotated character
        return (c - base + key) % 26 + base;
    }
    else
    {
        // Return the character unchanged if it is not a letter
        return c;
    }
}