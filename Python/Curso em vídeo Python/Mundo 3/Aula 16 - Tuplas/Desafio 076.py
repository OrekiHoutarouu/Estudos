produtosEPrecos = ('Arroz', 4.63, 
                  'Feijão', 5.66,
                  'Nescau', 13.28,
                  'Mouse Gamer', 137.88,
                  'Gabinete Gamer', 230.99,
                  'Baqueta', 25.99,
                  'Guitarra', 1500.99,
                  'Lápis', 1,
                  'Borracha', 1.50,
                  'Garrafa', 24.99)

print('='*50)
print('LISTA DE VALORES'.center(50))
print('='*50)

for posicao in range(0, len(produtosEPrecos)):
    if posicao % 2 == 0:
        print(f'{produtosEPrecos[posicao]:.<30}',end='')
    else:
        print(f'R${produtosEPrecos[posicao]:>8.2f}')