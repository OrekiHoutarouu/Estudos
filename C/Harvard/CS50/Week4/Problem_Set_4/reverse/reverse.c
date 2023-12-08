#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#include "libs/wav.h"

int check_format(WAVHEADER header);
int get_block_size(WAVHEADER header);

int main(int argc, char *argv[])
{
    if (argc != 3)
    {
        printf("Usage: ./reverse input.wav output.wav\n");
        return 1;
    }

    char *infile = argv[1];
    FILE *inptr = fopen(infile, "rb");
    if (inptr == NULL)
    {
        printf("Couldn't open file.\n");
        return 1;
    }

    WAVHEADER header;
    fread(&header, sizeof(WAVHEADER), 1, inptr);

    if (check_format(header) == 0)
    {
        printf("Not a WAV file.\n");
        return 1;
    }

    if (header.audioFormat != 1)
    {
        printf("Not a WAV file.\n");
        return 1;
    }

    char *outfile = argv[2];
    FILE *outptr = fopen(outfile, "wb");
    if (outptr == NULL)
    {
        printf("Couldn't open file.\n");
        return 1;
    }

    fwrite(&header, sizeof(WAVHEADER), 1, outptr);

    int size = get_block_size(header);

    if (fseek(inptr, size, SEEK_END))
    {
        return 1;
    }

    BYTE buffer[size];
    while (ftell(inptr) - size > sizeof(header))
    {
        if (fseek(inptr, -2 * size, SEEK_CUR))
        {
            return 1;
        }
        fread(buffer, size, 1, inptr);
        fwrite(buffer, size, 1, outptr);
    }
    fclose(outptr);
    fclose(inptr);
}

int check_format(WAVHEADER header)
{
    if (header.format[0] == 'W' && header.format[1] == 'A' && header.format[2] == 'V' && header.format[3] == 'E')
    {
        return 1;
    }
    return 0;
}

int get_block_size(WAVHEADER header)
{
    int size = header.numChannels + header.bitsPerSample / 8;
    return size;
}
