# Recover - CS50x 2024

[CS50 Recover Problem Set](https://cs50.harvard.edu/x/2024/psets/4/recover/)

## Overview
In this problem set, you will create a program in C to recover JPEG images from a forensic image of a memory card. The program will scan the memory card for JPEG signatures and extract the images.

## Objectives
- Implement a program to recover JPEGs from a memory card image.
- Handle file I/O operations and work with raw byte data.
- Ensure proper memory management.

## Instructions

1. **Download Code**: Download and unzip the distribution code.
2. **Open Memory Card**: Open the provided `card.raw` file.
3. **Scan for JPEGs**: Implement logic to detect JPEG signatures and recover images.
4. **Save JPEGs**: Save each recovered image as `###.jpg`.

## Example
```sh
$ ./recover card.raw
```