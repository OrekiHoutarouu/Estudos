produtosEPreços = ('Arroz', 4.63, 
                  'Feijão', 5.66,
                  'Nescau', 13.28,
                  'Mouse Gamer', 137.88,
                  'Gabinete Gamer', 230.99,
                  'Baqueta', 25.99,
                  'Guitarra', 1500.99,
                  'Lápis', 1,
                  'Borracha', 1.50,
                  'Garrafa', 24.99)

print(f'{"-"*50}\n{"LISTA DE VALORES":^50}\n{"-"*50}')

for posição in range(0, len(produtosEPreços)):
    if posição % 2 == 0:
        print(f'{produtosEPreços[posição]:.<30}',end='')
    else:
        print(f'R${produtosEPreços[posição]:>8.2f}')