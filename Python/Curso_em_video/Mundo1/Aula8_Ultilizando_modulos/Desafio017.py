import math

catetoAdjacente = float(input('Digite o valor do cateto adjacente: '))
catetoOposto = float(input('Digite o valor do cateto oposto: '))

print(f'O valor da hipotenusa desse triângulo retângulo é de {math.sqrt((catetoAdjacente ** 2) + (catetoOposto ** 2)):.2f}.')