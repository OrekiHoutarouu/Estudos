#include <stdio.h>

int main(void)
{   
    int counter = 0;

    printf("Using while:\n");
    while (counter < 3)
    {
        printf("meow\n");
        counter++;
    }
    
    printf("Using for:\n");
    for (int counter = 0; counter < 3; counter++)
    {
        printf("meow\n");
    }   
    
}
