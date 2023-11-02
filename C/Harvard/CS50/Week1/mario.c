#include <stdio.h>
#include "libs/cs50.c"

int get_size(void);
void print_grid(int numberOfBricks);

int main(void)
{
    int numberOfBricks = get_size();
    
    print_grid(numberOfBricks);
}


int get_size(void)
{
    int numberOfBricks;
    do
    {
        numberOfBricks = get_int("Size: ");
    } 
    while (numberOfBricks < 1);
    
    return numberOfBricks;
}


void print_grid(int numberOfBricks)
{
    for (int column = 0; column < numberOfBricks; column++)
    {
        for (int row = 0; row < numberOfBricks; row++)
        {
            printf("#");
        }
        printf("\n"); 
    }
}