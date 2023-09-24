palavras = ('correr', 'pular', 'andar', 'voar', 'dançar', 'brincar', 'beber', 'comer', 'beijar', 'abraçar')
for palavra in palavras:
    print(f'\nNa palavra {palavra} temos as vogais ',end='')
    for letra in palavra:
            if letra.lower() in 'aeiou':
                print(letra, end=' ')