#include "cs50.c"
#include <stdio.h>

int main(void)
{
    string answer = get_string(answer, "What's your name?");
    printf("Hello, %s!\n", answer);
}