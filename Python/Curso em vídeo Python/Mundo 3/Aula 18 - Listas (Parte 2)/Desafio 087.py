matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaDosPares = somaDaTerceiraColuna = maiorDaSegundaLinha = 0

for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite um valor para {linha, coluna}: '))

print('='*60)

for linha in range(0,3):
    
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        
        if matriz[linha][coluna] % 2 == 0:
            somaDosPares += matriz[linha][coluna]
            
    print()
            
print(f'A soma dos dígitos pares é igual a {somaDosPares}')

for linha in range(0,3):
    somaDaTerceiraColuna += matriz[linha][2]
print(f'A soma dos dígitos da terceira coluna é igual a {somaDaTerceiraColuna}')

for coluna in range(0,3):
    
    if coluna == 0:
        maiorDaSegundaLinha = matriz[1][coluna]
    elif matriz[1][coluna] > maiorDaSegundaLinha:
        maiorDaSegundaLinha = matriz[1][coluna]
        
print(f'O maior dígito da segunda linha é {maiorDaSegundaLinha}')