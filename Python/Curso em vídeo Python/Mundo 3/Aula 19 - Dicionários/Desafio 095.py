jogador = {}
gols = []
time = []

while True:
    
    jogador['Nome'] = str(input('Nome do jogador: ')).strip()
    partidas = int(input(f'Quantas partidas o jogador {jogador["Nome"]} jogou? '))
    
    for golsNaPartida in range(partidas):
        gols.append(int(input(f'Quantos gols na partida {golsNaPartida + 1}? ')))
        jogador['Gols'] = gols[:]
        jogador['Total'] = sum(gols)
        
    gols.clear()
    
    time.append(jogador.copy())
    
    while True:
        
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()
        
        if continuar in 'SN':
            break
        
        else:
            print('Valor inválido, digite apenas S ou N.')
            
    if continuar in 'N':
        break

print('='*50)
print(f'{"No.":<5}{"Nome":<10}{"Gols":<20}{"Total":<30}')
print('='*50)

for chave, valor in enumerate(time):
    print(f'{chave:<5}', end='')
    print(f'{valor["Nome"]:<10}', end='')
    print(f'{valor["Gols"]}', end='')
    print(f'{valor["Total"]:>18}') 
    
print('='*50)

numeroDoJogador = 0
  
while numeroDoJogador != 999:
    numeroDoJogador = int(input('Deseja ver as informações de qual jogador? (999 interrompe): '))
    
    if numeroDoJogador >= len(time):
        print('Valor inválido, digite o valor numérico correspondente a algum jogador.')
        
    else:
        print(f'Levantamento do jogador {time[numeroDoJogador]["Nome"]}')
        for chave, valor in enumerate(time[numeroDoJogador]['Gols']):
            print(f'No jogo {chave}, fez {valor} gols.')