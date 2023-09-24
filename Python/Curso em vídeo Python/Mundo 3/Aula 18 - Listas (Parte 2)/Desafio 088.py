from random import randint
conjuntoDeNúmeros = []
números = []
contador = 0

print('=' * 40)
print('               MEGA SENA')
print('=' * 40)
print()

jogos = int(input('Quantos jogos deseja sortear? '))

print()
print('JOGOS')
print()

for aleatórios in range(jogos):
    
    for repetições in range(0,6):
        números.append(randint(0, 60))
        
        if len(números) == 6:
                conjuntoDeNúmeros.append(números[:])
                números.clear()


for ordem in conjuntoDeNúmeros:
    print(f'Jogo {contador + 1}: {ordem} ')
    contador += 1
    
print()
print('Boa sorte!')