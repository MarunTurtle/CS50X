// Write a function to replace vowels with numbers
// Get practice with strings
// Get practice with command line
// Get practice with switch

#include <cs50.h>
#include <stdio.h>
#include <string.h>

string replace(string input_string);

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: %s <input_string>\n", argv[0]);
        return 1;
    }
    printf("%s\n", replace(argv[1]));
}

string replace(string input_string)
{
    int length = strlen(input_string);
    for (int i = 0; i < length; i++)
    {
        switch (input_string[i])
        {
            case 'a':
            case 'A':
                input_string[i] = '6';
                break;

            case 'e':
            case 'E':
                input_string[i] = '3';
                break;

            case 'i':
            case 'I':
                input_string[i] = '1';
                break;

            case 'o':
            case 'O':
                input_string[i] = '0';
                break;
        }
    }
    return input_string;
}


