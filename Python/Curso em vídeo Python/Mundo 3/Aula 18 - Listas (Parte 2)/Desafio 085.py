numeros = [[], []]

for contador in range(7):
    
    valores = int(input(f'Digite o {contador}° valor: '))
    
    if valores % 2 == 0:
        numeros[0].append(valores)
        
    else:
        numeros[1].append(valores)

numeros[0].sort()
numeros[1].sort()

print('='*60)

print(f'Os valores pares digitados foram: {numeros[0]}.')
print(f'Os valores ímpares digitados foram: {numeros[1]}.')