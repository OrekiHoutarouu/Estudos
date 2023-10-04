distancia = float(input('Qual a distância em km da sua viagem?: '))

if distancia < 200:
    print(f'O valor da viagem será de R${(distancia * 0.5):.2f}.')
    
else:
    print(f'O valor da viagem será de R${(distancia * 0.45):.2f}.')    