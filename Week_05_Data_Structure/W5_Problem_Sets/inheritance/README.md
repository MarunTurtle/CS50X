# Inheritance - CS50x 2024
[CS50 Inheritance Problem Set](https://cs50.harvard.edu/x/2024/psets/5/inheritance/)

## Overview
In this problem set, you will create a program in C to simulate the inheritance of blood types across generations. Each person's blood type is determined by alleles inherited from their parents.

## Objectives
- Simulate the inheritance of blood types.
- Use recursion to create family generations.
- Manage dynamic memory allocation.

## Instructions

1. **Download Code**: Download and unzip the distribution code.
2. **Implement `create_family`**: Recursively create family generations.
3. **Implement `free_family`**: Free allocated memory for the family tree.
4. **Assign Alleles**: Randomly assign alleles for the oldest generation and inherit alleles for younger generations.

## Example

```sh
$ ./inheritance
Child (Generation 0): blood type OO
    Parent (Generation 1): blood type AO
        Grandparent (Generation 2): blood type OA
        Grandparent (Generation 2): blood type BO
    Parent (Generation 1): blood type OB
        Grandparent (Generation 2): blood type AO
        Grandparent (Generation 2): blood type BO
```