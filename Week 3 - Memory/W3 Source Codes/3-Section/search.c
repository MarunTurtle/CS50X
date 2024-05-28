#include <cs50.h>
#include <stdio.h>

// Definition of the candidate struct
typedef struct
{
    string name; // Name of the candidate
    int votes;   // Number of votes for the candidate
} candidate;

// Declaration of an array to hold candidates
const int num_candidates = 4;
candidate candidates[num_candidates];

int main(void)
{
    // Example usage
    // Initialize candidates
    candidates[0].name = "Candidate 1";
    candidates[0].votes = 10;

    candidates[1].name = "Candidate 2";
    candidates[1].votes = 20;

    candidates[2].name = "Candidate 3";
    candidates[2].votes = 30;

    candidates[3].name = "Candidate 4";
    candidates[3].votes = 40;

    // Example of printing candidate names and votes
    for (int i = 0; i < num_candidates; i++)
    {
        printf("%s has %d votes.\n", candidates[i].name, candidates[i].votes);
    }

    // Find highest number of votes
    int highest_votes = 0;
    for (int i = 0; i < num_candidates; i++)
    {
        if (highest_votes < candidates[i].votes)
        {
            highest_votes = candidates[i].votes;
        }
    }

    // Find the name of the candidate with the highest nubmer of votes
    string winner;
    for (int i = 0; i < num_candidates; i++)
    {
        if (candidates[i].votes == highest_votes)
        {
            winner = candidates[i].name;
        }
    }

    // Print the highest number of votes and their name
    printf("The winner is %s with %i votes\n", winner, highest_votes);
}
