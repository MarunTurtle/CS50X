#include <cs50.h>
#include <stdio.h>

// Function prototype for checking if a number is prime
bool prime(int number);

int main(void)
{
    int min;
    // Prompt user for minimum value, ensuring it is at least 1
    do
    {
        min = get_int("Minimum: ");
    }
    while (min < 1);

    int max;
    // Prompt user for maximum value, ensuring it is greater than min
    do
    {
        max = get_int("Maximum: ");
    }
    while (min >= max);

    // Iterate through the range from min to max
    for (int i = min; i <= max; i++)
    {
        // Print the number if it is prime
        if (prime(i))
        {
            printf("%i\n", i);
        }
    }
}

// Function to check if a number is prime
bool prime(int number)
{
    // Numbers less than 2 are not prime
    if (number < 2)
    {
        return false;
    }

    // Check divisibility from 2 up to the square root of the number
    for (int i = 2; i * i <= number; i++)
    {
        // If number is divisible by any i, it is not prime
        if (number % i == 0)
        {
            return false;
        }
    }
    // If no divisors were found, the number is prime
    return true;
}