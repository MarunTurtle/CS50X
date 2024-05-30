#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char rotate(char c, int key);

int main(int argc, string argv[])
{
    // Check command-line argument
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    // Check if argv[1] contains only digits
    for (int i = 0, n = strlen(argv[1]); i < n; i++)
    {
        if (!isdigit(argv[1][i]))
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }

    // Convert argv[1] to an integer
    int key = atoi(argv[1]);

    // Ask for plaintext
    string plaintext = get_string("plaintext: ");

    // Output ciphertext header
    printf("ciphertext: ");

    // Encrypt and print each character in the plaintext
    for (int i = 0, n = strlen(plaintext); i < n; i++)
    {
        char cipher_char = rotate(plaintext[i], key);
        printf("%c", cipher_char);
    }

    printf("\n");

    return 0;
}

// Function to rotate a character by a given key
char rotate(char c, int key)
{
    if (isalpha(c))
    {
        // Determine whether the character is uppercase or lowercase
        // Apply the Caesar cipher formula
        char base;

        if (isupper(c))
        {
            base = 'A';
        }
        else
        {
            base = 'a';
        }
        return (c - base + key) % 26 + base;
    }
    else
    {
        // If the character is not a letter, leave it unchanged
        return c;
    }
}
