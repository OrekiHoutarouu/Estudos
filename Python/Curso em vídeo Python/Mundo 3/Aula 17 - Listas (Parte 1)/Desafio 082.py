valores = []
valoresPares = []
valoresÍmpares = []

while True:
    números = (int(input('Digite um valor: ')))
    valores.append(números)
    
    if números % 2 == 0:
        valoresPares.append(números)
        
    else:
        valoresÍmpares.append(números)
    
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if continuar == 'N':
        break
    
print('Os números digitados foram: ', end='')
for números in valores:
    print(f'{números} ', end='')

print('\nOs números pares digitados foram: ', end='')
for númerosPares in valoresPares:
    print(f'{númerosPares} ', end='')
    
print('\nOs números ímpares digitados foram: ', end='')
for númerosÍmpares in valoresÍmpares:
    print(f'{númerosÍmpares} ', end='')