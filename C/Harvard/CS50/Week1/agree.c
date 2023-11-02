#include "cs50.c"
#include <stdio.h>

int main(void)
{
    char yesOrNo = get_char("Do you agree? ");

    if (yesOrNo == 'y' || yesOrNo == 'Y') 
    {
        printf("Agreed\n");
    }
    else if (yesOrNo == 'n' || yesOrNo == 'N')
    {
        printf("Not agreed\n");
    }
}