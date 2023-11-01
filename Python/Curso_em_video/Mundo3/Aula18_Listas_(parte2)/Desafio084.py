nomeEPeso = []
pessoas = []

while True:
    
    nomeEPeso.append(str(input('Nome: ')).strip())
    nomeEPeso.append(int(input('Peso: ')))
    
    if len(pessoas) == 0:
        maiorPeso = menorPeso = nomeEPeso[1]
        
    else:
        
        if nomeEPeso[1] > maiorPeso:
            maiorPeso = nomeEPeso[1]
            
        if nomeEPeso[1] < menorPeso:
            menorPeso = nomeEPeso[1]
            
    pessoas.append(nomeEPeso[:])
    nomeEPeso.clear()
    
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if continuar in 'N':
        break

print('='*60)

print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'O menor peso registrado foi {menorPeso}kg, de ', end='')
        
for nome in pessoas:
    
    if nome[1] == menorPeso:
        print(f'{nome[0]} ', end='')
        
print(f'\nO maior peso registrado foi {maiorPeso}kg, de ', end='')
       
for nomes in pessoas:
    
    if nomes[1] == maiorPeso:
        print(f'{nomes[0]} ', end='')