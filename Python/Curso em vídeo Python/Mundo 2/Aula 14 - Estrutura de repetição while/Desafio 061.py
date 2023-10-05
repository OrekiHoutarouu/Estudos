primeiroTermo = int(input('Digite o primeiro termo da Progressão aritimética: '))
razao = int(input('Digite a razão da progressão aritimética: '))

contador = 1

while contador < 11:
    print(f'O {contador}° termo dessa progressão aritimética é {primeiroTermo}')
    primeiroTermo += razao
    contador += 1