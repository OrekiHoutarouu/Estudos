velocidade = int(input('Digite a velocidade do carro em km/h: '))

if velocidade > 80:
    print(f'O carro foi multado num valor de R${((velocidade - 80) * 7):.2f}.')
    
else:
    print('O carro não ultrapassou a velocidade limite da via.')    