valores = []
for contador in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

print('Os números digitados foram ', end='')
for lista in valores:
    print(lista, end=' ')
    
print(f'\nO maior número digitado foi {max(valores)}. Na(s) posição(ões): ', end='')
for indice, valor in enumerate(valores):
    if valor == max(valores):
        print(f'{indice + 1} ', end='')
        
print(f'\nE o menor valor digitado foi {min(valores)}. Na(s) posição(ões): ', end='')
for indice, valor in enumerate(valores):
    if valor == min(valores):
        print(f'{indice + 1} ', end='')