primeiroTermo = int(input('Digite o primeiro termo da Progressão Aritimética: '))
razao = int(input('Digite a razão da Progressão Aritimética: '))

for contador in range(1, 11):
    print(f'O {contador}° termo dessa Progressão Aritimética é {primeiroTermo}.')
    
    primeiroTermo += razao