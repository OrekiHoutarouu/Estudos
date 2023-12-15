from cs50 import get_int


def main():
    cardNumber = get_int("Number: ")
    sumOfCardNumbers = sumAndMultiplyCardNumbers(cardNumber)
    cardNumberLength = len(str(cardNumber))

    if validateCardNumber(sumOfCardNumbers) == True:
        if (
            cardNumberLength == 15
            and str(cardNumber)[:2] == "34"
            or str(cardNumber)[:2] == "37"
        ):
            print("AMEX")

        elif (
            cardNumberLength == 16
            and str(cardNumber)[:2] == "51"
            or str(cardNumber)[:2] == "52"
            or str(cardNumber)[:2] == "53"
            or str(cardNumber)[:2] == "54"
            or str(cardNumber)[:2] == "55"
        ):
            print("MASTERCARD")

        elif (
            cardNumberLength == 13
            or cardNumberLength == 16
            and str(cardNumber)[:1] == "4"
        ):
            print("VISA")

        else:
            print("INVALID")

    else:
        print("INVALID")


def sumAndMultiplyCardNumbers(cardNumber):
    sumOfCardNumbers = 0
    isEveryOtherDigit = False

    while cardNumber > 0:
        if isEveryOtherDigit == True:
            lastEveryOtherDigit = int(cardNumber) % 10
            multiply = lastEveryOtherDigit * 2

            lastMultipliedDigit = 1
            while lastMultipliedDigit > 0:
                lastMultipliedDigit = int(multiply) % 10
                sumOfCardNumbers += lastMultipliedDigit
                multiply /= 10
                lastMultipliedDigit = int(multiply)

        else:
            lastDigit = int(cardNumber) % 10
            sumOfCardNumbers += lastDigit

        isEveryOtherDigit = not isEveryOtherDigit
        cardNumber /= 10

    return int(sumOfCardNumbers)


def validateCardNumber(sumOfCardNumbers):
    if int(sumOfCardNumbers) % 10 == 0:
        return True

    else:
        return False


if __name__ == "__main__":
    main()
