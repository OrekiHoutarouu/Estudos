n = str(input(('Digite uma palavra sem acentos para saber se é um palíndromo: '))).replace(' ','').upper().strip()
ni = n[::-1]
print(f'{n} ao contrário é {ni}, ou seja ',end='')
if ni == n:
    print('a palavra digitada é um palíndromo!')
else:
    print('a palavra digitada não é um palíndromo!')