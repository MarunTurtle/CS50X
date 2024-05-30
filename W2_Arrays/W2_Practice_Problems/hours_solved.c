#include <cs50.h>
#include <ctype.h>
#include <stdio.h>

// Function prototype for calculating hours
float calc_hours(int hours[], int weeks, char output);

int main(void)
{
    // Get the number of weeks from the user
    int weeks = get_int("Number of weeks taking CS50: ");
    int hours[weeks];

    // Get the number of hours spent on homework each week
    for (int i = 0; i < weeks; i++)
    {
        hours[i] = get_int("Week %i HW Hours: ", i);
    }

    // Prompt user for output preference: total or average hours
    char output;
    do
    {
        output = toupper(get_char("Enter T for total hours, A for average hours per week: "));
    }
    while (output != 'T' && output != 'A');

    // Print the calculated hours based on user preference
    printf("%.1f hours\n", calc_hours(hours, weeks, output));
}

// Function to calculate total or average hours
float calc_hours(int hours[], int weeks, char output)
{
    int sum = 0;

    // Sum up the hours for all weeks
    for (int i = 0; i < weeks; i++)
    {
        sum += hours[i];
    }

    // Return total hours if 'T' is selected
    if (output == 'T')
    {
        return sum;
    }
    // Return average hours if 'A' is selected
    else if (output == 'A')
    {
        return sum / (float) weeks;
    }
    return 0;
}