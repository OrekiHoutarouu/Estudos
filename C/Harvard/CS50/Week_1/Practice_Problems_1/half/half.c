#include "libs/cs50.c"
#include <stdio.h>

float half(float bill, float tax, int tip)
{
    bill = bill + ((bill * tax) / 100);
    bill = bill + ((bill * tip) / 100);
    bill /= 2;
    return bill;
}

int main(void)
{
    float bill_amount = get_float("Bill before tax and tip: ");
    float tax_percent = get_float("Sale Tax Percent: ");
    int tip_percent = get_int("Tip percent: ");

    printf("You will owe $%.2f each!\n", half(bill_amount, tax_percent, tip_percent));
}
