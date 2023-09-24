timesBrasileirão = 'Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico-PR', 'Atlético-MG', 'Fortaleza', 'São Paulo', 'Botafogo', 'América-MG', 'Santos', 'Goiás', 'Red Bull Bragantino', 'Coritiba', 'Cuiabá', 'Ceará', 'Atlético-GO', 'Avaí', 'Juventude'

print(f'Os 5 primeiros colocados do Campeonato Brasileiro de Futebol são: {timesBrasileirão[0]}, {timesBrasileirão[1]}, {timesBrasileirão[2]}, {timesBrasileirão[3]}, {timesBrasileirão[4]}')
print('-'*70)
print(f'Os 4 últimos colocados do Campeonato Brasileiro de Futebol são: {timesBrasileirão[-4]}, {timesBrasileirão[-3]}, {timesBrasileirão[-2]}, {timesBrasileirão[-1]}')
print('-'*70)
print(f'Todos os times do Campeonato Brasileiro de Futebol em ordem alfabética são: ',end='')
print(sorted(timesBrasileirão))
print('-'*70)
print(f'O Botafogo está na {timesBrasileirão.index("Botafogo")+1}° posição.')