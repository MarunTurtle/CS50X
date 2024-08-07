# Speller - CS50x 2024

[CS50 Speller Problem Set](https://cs50.harvard.edu/x/2024/psets/5/speller/)

## Overview

In this problem set, you will create a program in C to implement a spell checker using a hash table. The program will load a dictionary of words, check words against the dictionary, and report misspellings.

## Objectives

- **Implement a hash table** for fast dictionary lookups.
- **Handle file I/O operations** efficiently.
- **Ensure efficient memory usage** and avoid memory leaks.

## Instructions

1. **Download Code**: Download and unzip the distribution code.
2. **Implement Functions**: Complete the `load`, `hash`, `size`, `check`, and `unload` functions in `dictionary.c`.
3. **Test Program**: Use the provided texts and dictionaries to verify the correctness and efficiency of your implementation.

## Example

Run the program with the following command:

```sh
$ ./speller texts/lalaland.txt
```

This will check the spelling of words in `lalaland.txt` using your implemented spell checker.