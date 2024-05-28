#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

// Function prototypes
bool validate_key(string key);
string encrypt(string plaintext, string key);

int main(int argc, string argv[])
{
    // Check for the correct number of command-line arguments
    if (argc != 2)
    {
        printf("Usage: %s key\n", argv[0]);
        return 1;
    }

    // Validate the key
    string key = argv[1];
    if (!validate_key(key))
    {
        printf("Invalid key\n");
        return 1;
    }

    // Get plaintext from the user
    string plaintext = get_string("plaintext: ");

    // Encrypt and print the ciphertext
    string ciphertext = encrypt(plaintext, key);
    printf("ciphertext: %s\n", ciphertext);

    return 0;
}

// Function to validate the key
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

// Function to encrypt plaintext using the substitution cipher
string encrypt(string plaintext, string key)
{
    for (int i = 0, n = strlen(plaintext); i < n; i++)
    {
        if (isalpha(plaintext[i]))
        {
            char originalCase = isupper(plaintext[i]) ? 'A' : 'a';
            int keyIndex = toupper(plaintext[i]) - 'A';
            char encryptedChar = isupper(plaintext[i]) ? toupper(key[keyIndex]) : tolower(key[keyIndex]);
            plaintext[i] = encryptedChar;
        }
        // Skip non-alphabetic characters
    }

    return plaintext;
}
