dias = int(input('Por quantos dias você usou o carro? '))
quilometragem = float(input('E quantos km você rodou com o carro? '))

print(f'O valor do aluguel é de {(dias * 60) + (quilometragem * 0.15):.2f}.')