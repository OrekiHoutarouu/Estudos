jogador = {}
gols = []

jogador['Nome'] = str(input('Nome do jogador: ')).strip()
partidas = int(input(f'Quantas partidas o jogador {jogador["Nome"]} jogou? '))

for golsNaPartida in range(partidas):
    gols.append(int(input(f'Quantos gols na partida {golsNaPartida + 1}? ')))
    
jogador['Gols'] = gols[:]
jogador['Total'] = sum(gols)

print('='*50)
print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas.')

for chave, valor in enumerate(jogador['Gols']):
    print(f'Na partida {chave + 1}, {jogador["Nome"]} fez {valor} gol(s).')
    
print(f'{jogador["Nome"]} fez um total de {jogador["Total"]} gols.')