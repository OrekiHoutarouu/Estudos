from random import randint
from time import sleep
from operator import itemgetter

valoresSorteados = {'Jogador 1': randint(1, 6),
                    'Jogador 2': randint(1, 6),
                    'Jogador 3': randint(1, 6),
                    'Jogador 4': randint(1, 6)}

ranking = []

print(f'Valores sorteados:')
print()

for chave, valor in valoresSorteados.items():
    print(f'{chave} tirou {valor} no dado')
    sleep(0.5)

ranking = sorted(valoresSorteados.items(), key = itemgetter(1), reverse = True)

print('='*33)
print('Ranking'.center(33))
print()

for índice, valor in enumerate(ranking):
    print(f'{índice + 1}° lugar: {valor[0]} com {valor[1]} no dado')