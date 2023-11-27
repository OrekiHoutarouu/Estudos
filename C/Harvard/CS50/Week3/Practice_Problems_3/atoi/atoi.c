#include "libs/cs50.c"
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int convert(string input);

int main(void)
{
    string input = get_string(input, "Enter a positive integer: ");

    for (int i = 0, n = strlen(input); i < n; i++)
    {
        if (!isdigit(input[i]))
        {
            printf("Invalid Input!\n");
            return 1;
        }
    }

    printf("%i\n", convert(input));
}

int convert(string input)
{
    if (strlen(input) == 1)
    {
        return input[0] - '0';
    }

    char lastDigit = input[strlen(input) - 1];
    int convertedLastDigit = lastDigit - '0';
    input[strlen(input) - 1] = '\0';

    return convertedLastDigit + 10 * convert(input);
}
