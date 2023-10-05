print('='*50)
print('BANCO DO SAM'.center(50))
print('SÓ TEMOS NOTAS DE R$50, R$20 e R$1'.center(50))
print('='*50)

valorSacado = int(input('Digite o valor a ser sacado: '))

total = valorSacado
cedulaAtual = 50
totalCedulas = 0

while True:
    if total >= cedulaAtual:
        total -= cedulaAtual
        totalCedulas += 1
        
    else:
        if totalCedulas > 0:
            print(f'Total de {totalCedulas} cédula(s) de R${cedulaAtual}.')
            
        if cedulaAtual == 50:
            cedulaAtual = 20
            
        elif cedulaAtual == 20:
            cedulaAtual = 10
            
        elif cedulaAtual == 10:
            cedulaAtual = 1
    
        totalCedulas = 0
        if total == 0:
            break
        
        
print('='*50)
print('VOLTE SEMPRE AO BANCO DO SAM'.center(30))
print('='*50)