print(f'{"-"*20} LISTA DE PRODUTOS {"-"*20}')

totalGasto = acimaDeMil = menor = contador = 0
barato = ''
while True:
    print(f'{"="*59}')
    produto = str(input('Digite o nome do produto: '))
    preço = float(input('Digite o preço do produto: R$'))
    totalGasto += preço
    contador += 1
    
    if contador == 1 or preço < menor:
        menor = preço
        barato = produto
            
    if preço > 1000:
        acimaDeMil += 1
        
    continuar = ' '
    while continuar not in "SN":
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if continuar == "N":
        break
    
print(f'O total gasto nas compras foram de R${totalGasto:.2f}.\n{acimaDeMil} produto(s) passaram dos R$1000.\nO produto mais barato foi {barato} que custa R${menor:.2f}.')