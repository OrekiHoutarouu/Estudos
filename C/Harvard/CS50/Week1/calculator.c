#include "libs/cs50.c"
#include <stdio.h>

int main(void)
{
    long x = get_long("x: ");
    long y = get_long("y: ");
    double division = (double) x / (double) y;

    printf("%li / %li = %f", x, y, division);
}