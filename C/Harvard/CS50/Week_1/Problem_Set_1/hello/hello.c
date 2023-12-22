#include "libs/cs50.c"
#include <stdio.h>

int main(void)
{
    string name = get_string(name, "What's your name? ");
    printf("hello, %s\n", name);
}