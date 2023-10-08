numero = int(input('Digite um número para saber sua tabuada: '))

for contador in range (1, 11):
    print(f'{numero} x {contador} = {contador * numero}')