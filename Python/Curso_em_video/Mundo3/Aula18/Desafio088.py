from random import randint
conjuntoDeNumeros = []
numeros = []
contador = 0

print('='*50)
print('MEGA SENA'.center(50))
print('='*50)
print()

jogos = int(input('Quantos jogos deseja sortear? '))

print('='*50)
print('JOGOS'.center(50))
print('='*50)

for aleatorios in range(jogos):
    
    for repeticoes in range(0,6):
        numeros.append(randint(0, 60))
        
        if len(numeros) == 6:
                conjuntoDeNumeros.append(numeros[:])
                numeros.clear()


for ordem in conjuntoDeNumeros:
    print(f'Jogo {contador + 1}: {ordem} ')
    contador += 1
    
print()
print('Boa sorte!')