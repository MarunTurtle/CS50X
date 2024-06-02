#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

// Function prototypes
bool validate_key(string key);
string encrypt(string plaintext, string key);

int main(int argc, string argv[])
{
    // Ensure exactly one command-line argument is provided
    if (argc != 2)
    {
        printf("Usage: %s key\n", argv[0]);
        return 1;
    }

    // Validate the provided key
    string key = argv[1];
    if (!validate_key(key))
    {
        printf("Invalid key\n");
        return 1;
    }

    // Get plaintext input from the user
    string plaintext = get_string("plaintext: ");

    // Encrypt the plaintext and print the ciphertext
    string ciphertext = encrypt(plaintext, key);
    printf("ciphertext: %s\n", ciphertext);

    return 0;
}

// Validate the key: must be 26 unique alphabetic characters
bool validate_key(string key)
{
    if (strlen(key) != 26)
    {
        return false;
    }

    for (int i = 0; i < 26; i++)
    {
        if (!isalpha(key[i]))
        {
            return false;
        }

        // Check for duplicate characters
        for (int j = i + 1; j < 26; j++)
        {
            if (toupper(key[i]) == toupper(key[j]))
            {
                return false;
            }
        }
    }

    return true;
}

// Encrypt plaintext using the substitution cipher key
string encrypt(string plaintext, string key)
{
    for (int i = 0, n = strlen(plaintext); i < n; i++)
    {
        if (isalpha(plaintext[i]))
        {
            // Determine the case of the original character
            char originalCase = isupper(plaintext[i]) ? 'A' : 'a';
            // Find the corresponding key index
            int keyIndex = toupper(plaintext[i]) - 'A';
            // Encrypt the character, preserving the case
            char encryptedChar = isupper(plaintext[i]) ? toupper(key[keyIndex]) : tolower(key[keyIndex]);
            plaintext[i] = encryptedChar;
        }
        // Non-alphabetic characters remain unchanged
    }

    return plaintext;
}