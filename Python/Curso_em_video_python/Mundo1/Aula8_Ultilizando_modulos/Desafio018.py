from math import (sin, cos, tan, radians)

angulo = float(input('Digite o valor do ângulo: '))

print(f'O seno desse ângulo é {sin(radians(angulo)):.2f}, o cosseno é {cos(radians(angulo)):.2f} e o tangente é {tan(radians(angulo)):.2f}.')