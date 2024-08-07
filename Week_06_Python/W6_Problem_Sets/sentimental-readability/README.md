# Readability - CS50x 2024

[CS50 Readability Problem Set](https://cs50.harvard.edu/x/2024/psets/6/readability/)

## Overview
In this assignment, you will create a Python program to calculate the readability of a given text using the Coleman-Liau index. This index estimates the grade level required to understand the text.

## Objectives
- **Prompt User**: Request input text from the user.
- **Count Text Elements**: Calculate the number of letters, words, and sentences in the text.
- **Compute the Coleman-Liau Index**: Use the formula `index = 0.0588 * L - 0.296 * S - 15.8` to determine the readability score.
- **Output Grade Level**: Display the corresponding grade level based on the index.

## Instructions

1. **Prompt User**: Request the user to input a text.
2. **Count Text Elements**: Calculate the number of letters, words, and sentences in the input text.
3. **Compute the Coleman-Liau Index**: Use the formula:
   ```python
   index = 0.0588 * L - 0.296 * S - 15.8
   ```
   where `L` is the average number of letters per 100 words and `S` is the average number of sentences per 100 words.
4. **Output Grade Level**: Display the calculated grade level to the user.