#include "libs/cs50.c"
#include <stdio.h>

int main(void)
{
    int height;
    do
    {
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);

    for (int row = 0; row < height; row++)
    {
        for (int spaces = 0; spaces < height - row - 1; spaces++)
        {
            printf(" ");
        }

        for (int column = 0; column <= row; column++)
        {
            printf("#");
        }

        printf("  ");

        for (int column2 = 0; column2 <= row; column2++)
        {
            printf("#");
        }
        printf("\n");
    }
}
