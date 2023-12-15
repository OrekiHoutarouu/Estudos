from cs50 import get_int

height = 0
column = 0
column2 = 0
while height < 1 or height > 8:
    height = get_int("Height: ")

for row in range(height):
    for spaces in range(height - row - 1):
        print(" ", end="")

    while column <= row:
        print("#", end="")
        column += 1
    column = 0

    print("  ", end="")

    while column2 <= row:
        print("#", end="")
        column2 += 1
    column2 = 0

    print()
