valores = []
valoresPares = []
valoresImpares = []

while True:
    numeros = (int(input('Digite um valor: ')))
    valores.append(numeros)
    
    if numeros % 2 == 0:
        valoresPares.append(numeros)
        
    else:
        valoresImpares.append(numeros)
    
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if continuar == 'N':
        break
    
print('Os números digitados foram: ', end='')
for numeros in valores:
    print(f'{numeros} ', end='')

print('\nOs números pares digitados foram: ', end='')
for númerosPares in valoresPares:
    print(f'{númerosPares} ', end='')
    
print('\nOs números ímpares digitados foram: ', end='')
for númerosÍmpares in valoresImpares:
    print(f'{númerosÍmpares} ', end='')