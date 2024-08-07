# Plurality - CS50x 2024

[CS50 Plurality Problem Set](https://cs50.harvard.edu/x/2024/psets/3/plurality/)

## Overview

This problem set involves creating a program in C to simulate a plurality vote election. The program will determine the winner based on the highest number of votes.

## Objectives

- Handle command-line arguments for candidate names.
- Collect and count votes for each candidate.
- Print the name of the winning candidate(s).

## Instructions

1. **Command-Line Arguments**: Accept candidate names.
2. **Count Votes**: Implement the `vote` function to update vote totals.
3. **Print Winner**: Implement the `print_winner` function to display the winner(s).

## Example

```sh
$ ./plurality Alice Bob
Number of voters: 3
Vote: Alice
Vote: Bob
Vote: Alice
Alice
```