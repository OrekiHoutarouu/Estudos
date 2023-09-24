v = int(input('Digite a velocidade do carro em km/h: '))
if v > 80:
    print(f'O carro foi multado num valor de R${((v-80)*7):.2f}.')
else:
    print('O carro não ultrapassou a velocidade limite da via.')    