from math import (sin, cos, tan, radians)

ângulo = float(input('Digite o valor do ângulo: '))

print(f'O seno desse ângulo é {sin(radians(ângulo)):.2f}, o cosseno é {cos(radians(ângulo)):.2f} e o tangente é {tan(radians(ângulo)):.2f}.')