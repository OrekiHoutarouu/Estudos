print('='*50)
print('LISTA DE PRODUTOS'.center(50))
print('='*50)

totalGasto = acimaDeMil = menor = contador = 0
barato = ''

while True:
    print(f'{"="*50}')
    produto = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: R$'))
    totalGasto += preco
    contador += 1
    
    if contador == 1 or preco < menor:
        menor = preco
        barato = produto
            
    if preco > 1000:
        acimaDeMil += 1
        
    continuar = ' '
    while continuar not in "SN":
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()
        
    if continuar == "N":
        break
    
    
print(f'O total gasto nas compras foram de R${totalGasto:.2f}.\n{acimaDeMil} produto(s) passaram dos R$1000.\nO produto mais barato foi {barato} que custa R${menor:.2f}.')