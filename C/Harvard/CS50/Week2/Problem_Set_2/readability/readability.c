#include "libs/cs50.c"
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    string text = get_string(text, "Text: ");

    float letters = count_letters(text);
    float words = count_words(text);
    float sentences = count_sentences(text);
    float L = (letters / words) * 100;
    float S = (sentences / words) * 100;
    float grade = (0.0588 * L) - (0.296 * S) - 15.8;

    if (grade < 1)
    {
        printf("Before Grade 1\n");
    }

    else if (grade >= 16)
    {
        printf("Grade 16+\n");
    }

    else
    {
        printf("Grade %.0f\n", grade);
    }
}

int count_letters(string text)
{
    int letters = 0;
    for (int i = 0; i < strlen(text); i++)
    {
        if (isalpha(text[i]))
        {
            letters += 1;
        }
    }
    return letters;
}

int count_words(string text)
{
    int words = 1;
    for (int i = 0; i < strlen(text); i++)
    {
        if (isspace(text[i]))
        {
            words += 1;
        }
    }
    return words;
}

int count_sentences(string text)
{
    int sentences = 0;
    for (int i = 0; i < strlen(text); i++)
    {
        if ((text[i] == '!') || (text[i] == '?') || (text[i] == '.'))
        {
            sentences += 1;
        }
    }
    return sentences;
}
