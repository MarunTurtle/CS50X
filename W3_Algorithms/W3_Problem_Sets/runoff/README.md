# Runoff - CS50x 2024
[link](https://cs50.harvard.edu/x/2024/psets/3/runoff/)

## Overview
This problem set involves creating a program in C to simulate a runoff election using ranked-choice voting. Voters can rank candidates in order of preference, and the system will determine the winner through a series of elimination rounds.

## Objectives
- Handle command-line arguments for candidate names.
- Collect and process ranked votes.
- Implement functions to simulate runoff rounds and determine the winner.

## Instructions
1. **Command-Line Arguments**: Accept candidate names.
2. **Collect Votes**: Implement the `vote` function to record voter preferences.
3. **Runoff Rounds**: Implement `tabulate`, `print_winner`, `find_min`, `is_tie`, and `eliminate` functions.
4. **Output Winner**: Print the winner once one candidate has more than 50% of the votes.

## Example
```sh
$ ./runoff Alice Bob Charlie
Number of voters: 3
Rank 1: Alice
Rank 2: Charlie
Rank 3: Bob
Rank 1: Bob
Rank 2: Charlie
Rank 3: Alice
Rank 1: Charlie
Rank 2: Alice
Rank 3: Bob