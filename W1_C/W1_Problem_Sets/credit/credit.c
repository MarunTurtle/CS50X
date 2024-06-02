#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt user for card number
    long n;
    do
    {
        n = get_long("Number: ");
    }
    while (n < 0);

    // Determine the length of the card number
    int i = 0;
    long cc = n;
    while (cc > 0)
    {
        cc = cc / 10;
        i++;
    }

    // Validate card length (must be 13, 15, or 16 digits)
    if (i != 13 && i != 15 && i != 16)
    {
        printf("INVALID\n");
        return 0;
    }

    // Calculate checksum using Luhn's Algorithm
    int sum1 = 0;
    int sum2 = 0;
    long x = n;
    int total = 0;
    int mod1;
    int mod2;
    int d1;
    int d2;

    do
    {
        // Add last digit to sum1
        mod1 = x % 10;
        x = x / 10;
        sum1 = sum1 + mod1;

        // Process second last digit
        mod2 = x % 10;
        x = x / 10;

        // Double the digit and add the sum of its digits to sum2
        mod2 = mod2 * 2;
        d1 = mod2 % 10;
        d2 = mod2 / 10;
        sum2 = sum2 + d1 + d2;
    }
    while (x > 0);

    total = sum1 + sum2;

    // Validate checksum
    if (total % 10 != 0)
    {
        printf("INVALID\n");
        return 0;
    }

    // Extract starting digits to determine card type
    long start = n;
    do
    {
        start = start / 10;
    }
    while (start > 100);

    // Determine card type based on starting digits and length
    if ((i == 16) && (start / 10 == 5) && (0 < start % 10 && start % 10 < 6))
    {
        printf("MASTERCARD\n");
    }
    else if ((i == 15) && (start / 10 == 3) && (start % 10 == 4 || start % 10 == 7))
    {
        printf("AMEX\n");
    }
    else if (((i == 13) || (i == 16)) && (start / 10 == 4))
    {
        printf("VISA\n");
    }
    else
    {
        printf("INVALID\n");
    }
}