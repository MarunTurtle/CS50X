// Function prototype for replacing vowels with numbers
string replace(string input_string);

int main(int argc, string argv[])
{
    // Ensure exactly one command-line argument is provided
    if (argc != 2)
    {
        printf("Usage: %s <input_string>\n", argv[0]);
        return 1;
    }

    // Call the replace function and print the modified string
    printf("%s\n", replace(argv[1]));
}

// Function to replace vowels in the input string with specific numbers
string replace(string input_string)
{
    int length = strlen(input_string); // Get the length of the input string

    // Iterate over each character in the string
    for (int i = 0; i < length; i++)
    {
        // Replace vowels with corresponding numbers
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

    // Return the modified string
    return input_string;
}