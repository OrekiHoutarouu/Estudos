primeiroTermo = int(input('Digite o primeiro termo da Progressão Aritimética: '))
razao = int(input('Digite a razão da Progressão Aritimética: '))

for c in range(1, 11):
    print(f'O {c}° termo dessa Progressão Aritimética é {primeiroTermo}.')
    
    primeiroTermo += razao