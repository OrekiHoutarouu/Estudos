valores = []

while True:
    valores.append(int(input('Digite um número: ')))
    
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if continuar == 'N':
        break

print(f'Foram digitados {len(valores)} números')

valores.sort(reverse=True)
print('Os números digitados em ordem decrescente são: ', end='')
for números in valores:
    print(f'{números} ', end='')
    
if 5 not in valores:
    print('\nO número 5 não foi adicionado a lista.')
else:
    print('\nO número 5 foi adicionado na lista.')