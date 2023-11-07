#include "libs/cs50.c"
#include <stdio.h>

int main(void)
{
    string name = get_string(name, "What is your name? ");
    string location = get_string(location, "Where do you live? ");

    printf("Hello, %s, from %s!\n", name, location);
}
