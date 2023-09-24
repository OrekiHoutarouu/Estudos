valores = []

while True:
    números = (int(input('Digite um valor: ')))
    
    if números not in valores:
        valores.append(números)
        print('Número adicionado')
        
    else:
        print('Número repetido, digite outro.')
        
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if continuar == 'N':
        break
    
print('A lista com números não repetidos e em ordem crescente foi: ', end='')
valores.sort()
for lista in valores:
    print(f'{lista}', end=' ')