#include <stdio.h>
#include <string.h>
#include <cs50.h>

bool check_phrase(string);

int main(void)
{
    string phrase = get_string("What's the secret phrase? ");

    bool correct = check_phrase(phrase);

    if (correct == true)
    {
        printf("Come on in!\n");
    }
    else
    {
        printf("Access denied!\n");
    }
}

bool check_phrase(string phrase)
{
    string password = "Please";

    if (strcmp(phrase, password) == 0)
    {
        return true;
    }

    return false;
}
