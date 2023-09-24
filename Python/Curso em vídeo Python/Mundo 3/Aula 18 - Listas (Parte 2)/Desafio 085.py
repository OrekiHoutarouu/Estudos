números = [[], []]

for contador in range(7):
    
    valores = int(input(f'Digite o {contador}° valor: '))
    
    if valores % 2 == 0:
        números[0].append(valores)
    else:
        números[1].append(valores)

números[0].sort()
números[1].sort()

print('='*60)

print(f'Os valores pares digitados foram: {números[0]}')
print(f'Os valores ímpares digitados foram: {números[1]}')