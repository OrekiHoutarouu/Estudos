valores = (int(input('Digite um valor: ')),
           int(input('Digite outro valor: ')),
           int(input('Digite outro valor: ')),
           int(input('Digite o último valor: ')))

print(f'O valor 9 foi digitado {valores.count(9)} vez(es)')

if 3 in valores:
    print(f'O primeiro número 3 foi digitado na posição {valores.index(3)+1}')
else:
    print(f'O número 3 não foi digitado em nenhuma posição.')
    
print('O(s) número(s) par(es) digitado(s) foi(foram): ',end='')
for c in valores:
    if c % 2 == 0:
        print(c, end=' ')