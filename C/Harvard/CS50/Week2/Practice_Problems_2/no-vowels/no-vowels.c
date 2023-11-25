#include "libs/cs50.c"
#include <stdio.h>
#include <string.h>

string replace(string word);

int main(int argc, string argv[])
{
    if (argc <= 1 || argc > 2)
    {
        printf("Usage: ./no-vowels word\n");
        return 1;
    }

    else
    {
        printf("%s\n", replace(argv[1]));
        return 0;
    }
}

string replace(string word)
{
    for (int i = 0; i < strlen(word); i++)
    {
        switch (word[i])
        {
            case 'a':
                word[i] = '6';
                break;

            case 'e':
                word[i] = '3';
                break;

            case 'i':
                word[i] = '1';
                break;

            case 'o':
                word[i] = '0';
                break;
        }
    }
    return word;
}
