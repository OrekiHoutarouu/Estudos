#include "libs/cs50.c"
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SIZE_OF_ALPHABET 26
#define MAXCHAR 20

typedef struct node
{
    bool is_word;
    struct node *children[SIZE_OF_ALPHABET];
} node;

bool check(char *word);
bool unload(void);
void unloader(node *current);

node *root;

char name[MAXCHAR];

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./trie infile\n");
        return 1;
    }

    FILE *infile = fopen(argv[1], "r");
    if (!infile)
    {
        printf("Error opening file!\n");
        return 1;
    }

    root = malloc(sizeof(node));

    if (root == NULL)
    {
        return 1;
    }

    root->is_word = false;
    for (int i = 0; i < SIZE_OF_ALPHABET; i++)
    {
        root->children[i] = NULL;
    }

    while (fscanf(infile, "%s", name) == 1)
    {
        node *cursor = root;

        for (int i = 0, n = strlen(name); i < n; i++)
        {
            int index = tolower(name[i]) - 'a';
            if (cursor->children[index] == NULL)
            {
                node *new = malloc(sizeof(node));
                new->is_word = false;
                for (int j = 0; j < SIZE_OF_ALPHABET; j++)
                {
                    new->children[j] = NULL;
                }
                cursor->children[index] = new;
            }

            cursor = cursor->children[index];
        }

        cursor->is_word = true;
    }

    char *test; 

    if (check(test = get_string(test, "Check word: ")))
    {
        printf("Found!\n");
    }
    else
    {
        printf("Not Found.\n");
    }

    if (!unload())
    {
        printf("Problem freeing memory!\n");
        return 1;
    }

    fclose(infile);
}

bool check(char *word)
{
    node *cursor = root;

    for (int i = 0; i < strlen(word); i++)
    {
        int index = tolower(word[i]) - 'a';
        if (index < 0 || index >= SIZE_OF_ALPHABET)
        {
            return false;
        }

        if (cursor->children[index] == NULL)
        {
            return false;
        }

        cursor = cursor->children[index];
    }
    return cursor->is_word;
}

bool unload(void)
{
    unloader(root);

    return true;
}

void unloader(node *current)
{
    for (int i = 0; i < SIZE_OF_ALPHABET; i++)
    {
        if (current->children[i] != NULL)
        {
            unloader(current->children[i]);
        }
    }

    free(current);
}
