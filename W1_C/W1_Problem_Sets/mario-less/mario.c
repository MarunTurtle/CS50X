#include <cs50.h>
#include <stdio.h>

// Function prototypes
int get_height(void);
void print_grid(int height);

int main(void)
{
    // Get the height from the user
    int height = get_height();
    
    // Print the grid based on the height
    print_grid(height);
}

// Prompt user for a valid height between 1 and 8
int get_height(void)
{
    int height;
    do
    {
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8); // Ensure height is within the valid range
    return height;
}

// Print a grid of '#' characters of the specified height
void print_grid(int height)
{
    for (int i = 1; i <= height; i++)
    {
        // Print leading spaces
        for (int j = 0; j < height - i; j++)
        {
            printf(" ");
        }

        // Print '#' characters
        for (int k = 0; k < i; k++)
        {
            printf("#");
        }

        // Move to the next line
        printf("\n");
    }
}