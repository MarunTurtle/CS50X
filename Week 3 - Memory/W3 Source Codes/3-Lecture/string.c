#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
     // An array of integers
    string strings[] = {"battleship", "boot", "cannon", "iron", "thimble", "top hat"};

    // Search for number
    string s = get_string("String: ");
    for (int i = 0; i < 6; i++)
    {
        if (strcmp(strings[i], s) == 0)
        {
            printf("Found\n");
            return 0;
        }
    }
    printf("Not found\n");
    return 1;
}
