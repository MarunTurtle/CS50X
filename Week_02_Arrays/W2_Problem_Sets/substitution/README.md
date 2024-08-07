# Substitution Cipher - CS50x 2024

[CS50 Substitution Cipher Problem Set](https://cs50.harvard.edu/x/2024/psets/2/substitution/)

## Overview

This problem set involves creating a program in C to encrypt messages using a substitution cipher. The program replaces each letter in the plaintext with another letter based on a provided key.

## Objectives

- Implement a substitution cipher for text encryption.
- Handle command-line arguments and input validation.
- Preserve the case of the letters.

## Instructions

1. **Command-Line Argument**: Accept a 26-character key.
2. **Validate Key**: Ensure it contains each letter exactly once and is alphabetic.
3. **Prompt for Plaintext**: Get plaintext input from the user.
4. **Encrypt Text**: Apply the cipher, preserving case.
5. **Output Ciphertext**: Display the encrypted text.

## Example

```sh
$ ./substitution NQXPOMAFTRHLZGECYJIUWSKDVB
plaintext: HELLO
ciphertext: FOLLE
```