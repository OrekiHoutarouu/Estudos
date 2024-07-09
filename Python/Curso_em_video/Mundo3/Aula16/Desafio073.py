timesBrasileirao = 'Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico-PR', 'Atlético-MG', 'Fortaleza', 'São Paulo', 'Botafogo', 'América-MG', 'Santos', 'Goiás', 'Red Bull Bragantino', 'Coritiba', 'Cuiabá', 'Ceará', 'Atlético-GO', 'Avaí', 'Juventude'

print(f'Os 5 primeiros colocados do Campeonato Brasileiro de Futebol são: {timesBrasileirao[0]}, {timesBrasileirao[1]}, {timesBrasileirao[2]}, {timesBrasileirao[3]}, {timesBrasileirao[4]}')
print('-'*70)
print(f'Os 4 últimos colocados do Campeonato Brasileiro de Futebol são: {timesBrasileirao[-4]}, {timesBrasileirao[-3]}, {timesBrasileirao[-2]}, {timesBrasileirao[-1]}')
print('-'*70)
print(f'Todos os times do Campeonato Brasileiro de Futebol em ordem alfabética são: ',end='')
print(sorted(timesBrasileirao))
print('-'*70)
print(f'O Botafogo está na {timesBrasileirao.index("Botafogo")+1}° posição.')