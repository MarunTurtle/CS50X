# Caesar - CS50x 2024
[link](https://cs50.harvard.edu/x/2024/psets/2/caesar/)

## Overview
This problem set involves creating a program in C to encrypt messages using Caesar's cipher. The program shifts each letter in the plaintext by a specified number of positions, preserving the case, and wraps around the alphabet if necessary.

## Objectives
- Implement Caesar's cipher for text encryption.
- Handle command-line arguments and input validation.

## Instructions
1. **Command-Line Argument**: Accept a non-negative integer key.
2. **Validate Input**: Ensure the key is a valid number.
3. **Prompt for Plaintext**: Get the plaintext input from the user.
4. **Encrypt Text**: Apply the cipher to each letter.
5. **Output Ciphertext**: Display the encrypted text.

## Example
```sh
$ ./caesar 1
plaintext:  HELLO
ciphertext: IFMMP