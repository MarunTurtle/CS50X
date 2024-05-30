 #include <stdio.h>
 #include <cs50.h>

 int main(void)
 {
    // Get the length from the user
    int length;
    do
    {
        length = get_int("Length: ");
    }
    while (length < 1);

    // Declare our array
    int twice[length];

    // Set the first value
    twice[0] = 1;
    printf("%i\n", twice[0]);

    for (int i = 1; i < length; i++)
    {
        // Make the current element twice the previous
        twice[i] = twice[i - 1] * 2;

        // Print the current element
        printf("%i\n", twice[i]);
    }

 }
