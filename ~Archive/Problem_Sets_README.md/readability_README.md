# Readability - CS50x 2024
[link](https://cs50.harvard.edu/x/2024/psets/2/readability/)

## Overview
This problem set involves creating a program in C to calculate the readability of text using the Coleman-Liau index, which estimates the grade level needed to understand the text.

## Objectives
- Prompt the user for text input.
- Calculate the number of letters, words, and sentences.
- Compute the Coleman-Liau index.
- Print the corresponding grade level.

## Instructions
1. **Prompt User**: Request input text.
2. **Count Text Elements**: Calculate letters, words, and sentences.
3. **Compute Index**: Use the formula `index = 0.0588 * L - 0.296 * S - 15.8`.
4. **Output Grade Level**: Display the grade level.

## Example
```sh
$ ./readability
Text: Congratulations! Today is your day. You're off to Great Places! You're off and away!
Grade 3