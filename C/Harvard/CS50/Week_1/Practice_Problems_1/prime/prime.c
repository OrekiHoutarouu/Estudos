#include "libs/cs50.c"
#include <stdio.h>

bool prime(int number)
{
    int multiples = 0;

    for (int iterator = 1; iterator <= number - 1; iterator++)
    {
        if (number % iterator == 0)
        {
            multiples += 1;
        }
    }

    if (multiples >= 2)
    {
        return false;
    }

    else
    {
        return true;
    }
}

int main(void)
{
    int min;
    do
    {
        min = get_int("Minimum: ");
    }
    while (min < 1);

    int max;
    do
    {
        max = get_int("Maximum: ");
    }
    while (min >= max);

    for (int iterator = min; iterator <= max; iterator++)
    {
        if (prime(iterator))
        {
            printf("%i\n", iterator);
        }
    }
}