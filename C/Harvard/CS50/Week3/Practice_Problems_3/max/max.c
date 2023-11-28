#include "libs/cs50.c"
#include <stdio.h>

int max(int array[], int n);

int main(void)
{
    int n;
    do
    {
        n = get_int("Number of elements: ");
    }
    while (n < 1);

    int arr[n];

    for (int i = 0; i < n; i++)
    {
        arr[i] = get_int("Element %i: ", i);
    }

    printf("The max value is %i.\n", max(arr, n));
}

int max(int array[], int n)
{
    int maxValue = array[0];
    for (int i = 0; i < n; i++)
    {
        if (array[i + 1] == array[n])
        {
            break;
        }
        
        if (maxValue < array[i + 1])
        {
            maxValue = array[i + 1];
        }
    }

    return maxValue;
}
