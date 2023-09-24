r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))
if (r1 < r2 + r3) and (r2 < r1 + r3) and (r3 < r1 + r2):
    print('Essas retas podem formar um triângulo.')
    if r1 == r2 == r3:
        print('O triângulo é equilátero, pois todos os lados são iguais.')
    elif r1 == r2 != r3 or r1 == r3 != r2 or r2 == r3 != r1:
        print('O triângulo é isósceles, pois somente dois lados são iguais.')      
    else:
        print('O triângulo é escaleno, pois todos os lados são diferentes.')    
else:
    print('Essas retas não podem formar um triângulo.')