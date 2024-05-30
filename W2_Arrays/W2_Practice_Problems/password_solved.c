// Check that a password has at least one lowercase letter, uppercase letter, number, and symbol
// Practice iterating through a string
// Practice using the ctype library

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

// Function prototype for password validation
bool valid(string password);

int main(void)
{
    // Prompt user for password input
    string password = get_string("Enter your password: ");
    
    // Validate the password and provide feedback
    if (valid(password))
    {
        printf("Your password is valid!\n");
    }
    else
    {
        printf("Your password needs at least one uppercase letter, lowercase letter, number, and symbol\n");
    }
}

// Function to check if the password meets all criteria
bool valid(string password)
{
    int n = strlen(password);

    // Flags to track if each required character type is found
    bool hasLower = false;
    bool hasUpper = false;
    bool hasDigit = false;
    bool hasSymbol = false;

    // Iterate through each character in the password
    for (int i = 0; i < n; i++)
    {
        if (islower(password[i]))
        {
            hasLower = true;
        }
        else if (isupper(password[i]))
        {
            hasUpper = true;
        }
        else if (isdigit(password[i]))
        {
            hasDigit = true;
        }
        else if (ispunct(password[i]))
        {
            hasSymbol = true;
        }
    }

    // Return true if all required character types are present
    return hasLower && hasUpper && hasDigit && hasSymbol;
}