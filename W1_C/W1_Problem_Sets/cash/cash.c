#include <cs50.h>
#include <stdio.h>

// Function prototypes
int get_cents(void);
int calculate_quarters(int cents);
int calculate_dimes(int cents);
int calculate_nickels(int cents);
int calculate_pennies(int cents);

int main(void)
{
    // Get the amount of cents owed
    int cents = get_cents();

    // Calculate the number of quarters and update remaining cents
    int quarters = calculate_quarters(cents);
    cents -= quarters * 25;

    // Calculate the number of dimes and update remaining cents
    int dimes = calculate_dimes(cents);
    cents -= dimes * 10;

    // Calculate the number of nickels and update remaining cents
    int nickels = calculate_nickels(cents);
    cents -= nickels * 5;

    // Calculate the number of pennies and update remaining cents
    int pennies = calculate_pennies(cents);
    cents -= pennies * 1;

    // Sum total number of coins
    int coins = quarters + dimes + nickels + pennies;

    // Print total number of coins
    printf("%i\n", coins);
}

// Prompt user for a positive number of cents
int get_cents(void)
{
    int cents;
    do
    {
        cents = get_int("Change owed: ");
    }
    while (cents < 0);
    return cents;
}

// Calculate the number of quarters
int calculate_quarters(int cents)
{
    return cents / 25;
}

// Calculate the number of dimes
int calculate_dimes(int cents)
{
    return cents / 10;
}

// Calculate the number of nickels
int calculate_nickels(int cents)
{
    return cents / 5;
}

// Calculate the number of pennies
int calculate_pennies(int cents)
{
    return cents / 1;
}