#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct node
{
    char *phrase;
    struct node *next;
} node;

node *list = NULL;

node *n = malloc(sizeof(node));
n->phrase = "Hi!";
n->next = Null;

list = n;

// Inserting nodes

n = malloc(sizeof(node));
n->phrase = "Hey!";
n->next = list

list = n;

// Deallocate memories

node *ptr = list->next
free(list);
list = ptr;

ptr = list->next;





