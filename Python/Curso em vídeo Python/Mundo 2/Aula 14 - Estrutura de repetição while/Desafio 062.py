primeiroTermo = int(input('Digite o primeiro termo da Progressão Aritimética: '))
razao = int(input('Digite a razão da Progressão Aritimética: '))

contador = termosAMais = 1

while contador < 11:
    print(f'O {contador}° termo dessa Progressão Aritimética é {primeiroTermo}.')
    primeiroTermo += razao
    contador += 1
    
while termosAMais != 0:
    termosAMais = int(input('Quantos termos a mais deseja adicionar a essa Progressão Aritimética? Digite 0 caso não queira adicionar nenhum: '))
    
    for contador2 in range(termosAMais):
        print(f'O {contador}° termo dessa Progressão Aritimética é {primeiroTermo}.')
        contador += 1
        primeiroTermo += razao