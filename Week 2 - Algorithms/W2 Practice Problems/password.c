// Check that a password has at least one lowercase letter, uppercase letter, number and symbol
// Practice iterating through a string
// Practice using the ctype library

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

bool valid(string password);

int main(void)
{
    string password = get_string("Enter your password: ");
    if (valid(password))
    {
        printf("Your password is valid!\n");
    }
    else
    {
        printf("Your password needs at least one uppercase letter, lowercase letter, number and symbol\n");
    }
}
// TODO: Complete the Boolean function below
bool valid(string password)
{
    int n = strlen(password);

    // Flags to track if we have found each required character type
    bool hasLower = false;
    bool hasUpper = false;
    bool hasDigit = false;
    bool hasSymbol = false;

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

    // Check if all required character types are present
    return hasLower && hasUpper && hasDigit && hasSymbol;
}
