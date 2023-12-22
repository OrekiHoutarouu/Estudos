#include <stdio.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./read infile\n");
        return 1;
    }

    char buffer[7];

    char plates[8][7];

    FILE *infile = fopen(argv[1], "r");

    int idx = 0;

    while (fread(buffer, 1, 7, infile) == 7)
    {
        buffer[6] = '\0';

        for (int i = 0; i < 7; i++)
        {
            plates[idx][i] = buffer[i];
        }

        idx++;
    }
    fclose(infile);
    for (int i = 0; i < 8; i++)
    {
        printf("%s\n", plates[i]);
    }
}