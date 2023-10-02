distância = float(input('Qual a distância em km da sua viagem?: '))

if distância < 200:
    print(f'O valor da viagem será de R${(distância * 0.5):.2f}.')
    
else:
    print(f'O valor da viagem será de R${(distância * 0.45):.2f}.')    