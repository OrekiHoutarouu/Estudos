#include "helpers.h"
#include <math.h>

void grayscale(int height, int width, RGBTRIPLE image[height][width])
{

    for (int row = 0; row < height; row++)
    {
        for (int column = 0; column < width; column++)
        {
            int avarage =
                ((round(image[row][column].rgbtRed) + round(image[row][column].rgbtGreen) + round(image[row][column].rgbtBlue)) /
                     3.0 +
                 0.5);
            image[row][column].rgbtRed = avarage;
            image[row][column].rgbtGreen = avarage;
            image[row][column].rgbtBlue = avarage;
        }
    }
    return;
}

void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int row = 0; row < height; row++)
    {
        for (int column = 0; column < width / 2; column++)
        {
            RGBTRIPLE temp = image[row][column];

            image[row][column] = image[row][width - 1 - column];
            image[row][width - 1 - column] = temp;
        }
    }
    return;
}

void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];

    for (int row = 0; row < height; row++)
    {
        for (int column = 0; column < width; column++)
        {
            temp[row][column] = image[row][column];
        }
    }

    for (int row = 0; row < height; row++)
    {
        for (int column = 0; column < width; column++)
        {
            int red = 0;
            int green = 0;
            int blue = 0;
            float counter = 0.00;

            for (int x = -1; x < 2; x++)
            {
                for (int y = -1; y < 2; y++)
                {
                    int currentX = row + x;
                    int currentY = column + y;

                    if (currentX < 0 || currentX > (height - 1) || currentY < 0 || currentY > (width - 1))
                    {
                        continue;
                    }

                    red += image[currentX][currentY].rgbtRed;
                    green += image[currentX][currentY].rgbtGreen;
                    blue += image[currentX][currentY].rgbtBlue;

                    counter++;
                }
            }

            temp[row][column].rgbtRed = round(red / counter);
            temp[row][column].rgbtGreen = round(green / counter);
            temp[row][column].rgbtBlue = round(blue / counter);
        }
    }

    for (int row = 0; row < height; row++)
    {
        for (int column = 0; column < width; column++)
        {
            image[row][column] = temp[row][column];
        }
    }
    return;
}

void edges(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];

    for (int row = 0; row < height; row++)
    {
        for (int column = 0; column < width; column++)
        {
            temp[row][column] = image[row][column];
        }
    }

    int Gx[3][3] = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}};
    int Gy[3][3] = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}};

    for (int row = 0; row < height; row++)
    {
        for (int column = 0; column < width; column++)
        {
            int redX = 0;
            int greenX = 0;
            int blueX = 0;
            int redY = 0;
            int greenY = 0;
            int blueY = 0;

            for (int x = 0; x < 3; x++)
            {
                for (int y = 0; y < 3; y++)
                {
                    if (row - 1 + x < 0 || row - 1 + x > (height - 1) || column - 1 + y < 0 || column - 1 + y > (width - 1))
                    {
                        continue;
                    }

                    redX = redX + (image[row - 1 + x][column - 1 + y].rgbtRed * Gx[x][y]);
                    greenX = greenX + (image[row - 1 + x][column - 1 + y].rgbtGreen * Gx[x][y]);
                    blueX = blueX + (image[row - 1 + x][column - 1 + y].rgbtBlue * Gx[x][y]);

                    redY = redY + (image[row - 1 + x][column - 1 + y].rgbtRed * Gy[x][y]);
                    greenY = greenY + (image[row - 1 + x][column - 1 + y].rgbtGreen * Gy[x][y]);
                    blueY = blueY + (image[row - 1 + x][column - 1 + y].rgbtBlue * Gy[x][y]);
                }
            }

            int red = round(sqrt((redX * redX) + (redY * redY)));
            int green = round(sqrt((greenX * greenX) + (greenY * greenY)));
            int blue = round(sqrt((blueX * blueX) + (blueY * blueY)));

            if (red > 255)
            {
                red = 255;
            }

            if (green > 255)
            {
                green = 255;
            }

            if (blue > 255)
            {
                blue = 255;
            }

            temp[row][column].rgbtRed = red;
            temp[row][column].rgbtGreen = green;
            temp[row][column].rgbtBlue = blue;
        }
    }

    for (int row = 0; row < height; row++)
    {
        for (int column = 0; column < width; column++)
        {
            image[row][column].rgbtRed = temp[row][column].rgbtRed;
            image[row][column].rgbtGreen = temp[row][column].rgbtGreen;
            image[row][column].rgbtBlue = temp[row][column].rgbtBlue;
        }
    }
    return;
}