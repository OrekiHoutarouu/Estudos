from math import (sin, cos, tan, radians)
a = float(input('Digite o valor do ângulo: '))
print('O seno desse ângulo é {:.2f}, o cosseno é {:.2f} e o tangente é {:.2f}'.format(sin(radians(a)), cos(radians(a)), tan(radians(a))))