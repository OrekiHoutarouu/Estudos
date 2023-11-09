#include "libs/cs50.c"
#include <math.h>
#include <stdio.h>

int sumAndMultiplyCardNumbers(long long cardNumber)
{
    int sumOfCardNumbers = 0;
    bool isEveryOtherDigit = false;

    while (cardNumber > 0)
    {
        if (isEveryOtherDigit == true)
        {
            int lastEveryOtherDigit = cardNumber % 10;
            int multiply = lastEveryOtherDigit * 2;

            int lastMultipliedDigit = 1;
            while (lastMultipliedDigit > 0)
            {
                lastMultipliedDigit = multiply % 10;
                sumOfCardNumbers += lastMultipliedDigit;
                multiply /= 10;
                lastMultipliedDigit = multiply;
            }
        }

        else
        {
            int lastDigit = cardNumber % 10;
            sumOfCardNumbers += lastDigit;
        }

        isEveryOtherDigit = !isEveryOtherDigit;
        cardNumber /= 10;
    }

    return sumOfCardNumbers;
}


bool validateCardNumber(int sumOfCardNumbers)
{
    if (sumOfCardNumbers % 10 == 0)
    {
        return true;
    }

    else
    {
        return false;
    }
}


int getCardNumberLength(long long cardNumber)
{
    int counter = 0;
    while(cardNumber > 0)
    {
        cardNumber /= 10;
        counter++;
    }

    return counter;
}


int getCardFirstDigits(long long cardNumber, int cardNumberLength, int otherCardsOrVisa)
{
    long long powerForOtherCards = pow(10, (cardNumberLength - 2));
    long long powerForVisa = pow(10, (cardNumberLength - 1));

    long long firstCardDigits = cardNumber / powerForOtherCards;
    long long firstCardDigit = cardNumber / powerForVisa;

    if (otherCardsOrVisa == 1)
    {
        return firstCardDigit;
    }

    else
    {
        return firstCardDigits;
    }
}


int main(void)
{
    long long cardNumber = get_long_long("Number: ");
    int sumOfCardNumbers = sumAndMultiplyCardNumbers(cardNumber);
    int cardNumberLength = getCardNumberLength(cardNumber);
    long long firstCardDigits = getCardFirstDigits(cardNumber, cardNumberLength, 2);
    long long firstCardDigit = getCardFirstDigits(cardNumber, cardNumberLength, 1);

    if (validateCardNumber(sumOfCardNumbers) == true)
    {
        if ((cardNumberLength == 15) && (firstCardDigits == 34 || firstCardDigits == 37))
        {
            printf("AMEX\n");
        }

        else if ((cardNumberLength == 16) && (firstCardDigits == 51 || firstCardDigits == 52 || firstCardDigits == 53 || firstCardDigits == 54 || firstCardDigits == 55))
        {
            printf("MASTERCARD\n");
        }

        else if ((cardNumberLength == 13 || cardNumberLength == 16) && (firstCardDigit == 4))
        {
            printf("VISA\n");
        }

        else
        {
            printf("INVALID\n");
        }
    }

    else
    {
        printf("INVALID\n");
    }
}
