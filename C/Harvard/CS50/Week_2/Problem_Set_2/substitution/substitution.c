#include "libs/cs50.c"
#include <ctype.h>
#include <stdio.h>
#include <string.h>

string replace(string plaintext, string key);

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }

    if (strlen(argv[1]) < 26)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }

    for (int i = 0; i < strlen(argv[1]); i++)
    {
        if (!isalpha(argv[1][i]))
        {
            printf("Usage: ./substitution key\n");
            return 1;
        }
    }

    for (int i = 0; i < strlen(argv[1]); i++)
    {
        for (int j = i + 1; j < strlen(argv[1]); j++)
        {
            if (tolower(argv[1][j]) == tolower(argv[1][i]))
            {
                printf("Usage: ./substitution key\n");
                return 1;
            }
        }
    }

    string plaintext = get_string(plaintext, "plaintext: ");

    printf("ciphertext: %s\n", replace(plaintext, argv[1]));
    return 0;
}

string replace(string plaintext, string key)
{
    for (int i = 0; i < strlen(plaintext); i++)
    {
        int asciiValue = plaintext[i];
        if (isalpha(plaintext[i]))
        {
            if (islower(plaintext[i]))
            {
                plaintext[i] = tolower(key[asciiValue - 97]);
            }

            else
            {
                plaintext[i] = toupper(key[asciiValue - 65]);
            }
        }
    }

    return plaintext;
}
