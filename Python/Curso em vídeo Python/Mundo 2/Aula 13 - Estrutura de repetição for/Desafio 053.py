frase = str(input(('Digite uma frase sem acentos para saber se é um palíndromo: '))).upper().strip()
for caractere in '.!?,- ':
    frase = frase.replace(caractere, '')

print(f'{frase} ao contrário é {frase[::-1]}, ou seja ',end='')

if frase[::-1] == frase:
    print('a palavra digitada é um palíndromo!')
    
else:
    print('a palavra digitada não é um palíndromo!')