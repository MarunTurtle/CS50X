#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Get user's name
    string name = get_string("What is your name? ");
    
    // Get user's location
    string location = get_string("Where do you live? ");

    // Display greeting message
    printf("Hello, %s, from %s!\n", name, location);
}