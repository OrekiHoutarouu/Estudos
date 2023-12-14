import sys
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) > 1 and len(sys.argv) < 3 or len(sys.argv) > 3:
    print("Invalid usage")
    sys.exit(1)

elif len(sys.argv) == 1:
    input = str(input("Input: "))
    print(figlet.renderText(input))

elif len(sys.argv) == 3:
    if sys.argv[1] not in "-f" or sys.argv[1] not in "--font":
        print("Invalid usage")
        sys.exit(1)

    elif sys.argv[2] not in figlet.getFonts():
        print("Invalid usage")
        sys.exit(1)

    else:
        figlet.setFont(font=sys.argv[2])

        input = str(input("Input: "))
        print(figlet.renderText(input))
