#include <stdio.h>
#include "libs/cs50.c"

int main(void)
{
    int startingSize;
    do
    {
        startingSize = get_int("Start size: ");
    }
    while (startingSize < 9);

    int endingSize;
    do
    {
        endingSize = get_int("End size: ");
    }
    while (endingSize < startingSize);

    int yearsToEndingSize = 0;
    while (startingSize < endingSize)
    {
        startingSize += (startingSize / 3) - (startingSize / 4);
        yearsToEndingSize++;
    }

    printf("Years: %i\n", yearsToEndingSize);
}