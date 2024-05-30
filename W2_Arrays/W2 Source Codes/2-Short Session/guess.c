#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int number = 5;

    int guess = get_int("What's your guess? ");

    if (guess != number)
    {
        printf("Wrong guess!\n");
        return 0;
    }
    else (guess = number);
    {
        printf("You're correct!\n");
    }
}
