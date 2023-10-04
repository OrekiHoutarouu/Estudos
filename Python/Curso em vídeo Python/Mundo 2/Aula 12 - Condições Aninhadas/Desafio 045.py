from random import choice

opcoes = ['pedra', 'papel', 'tesoura']
escolhaComputador = choice(opcoes)

escolhaUsuario = str(input('Vamos jogar Jokenpô? Digite pedra, papel ou tesoura: ')).strip().lower()

if escolhaComputador == escolhaUsuario:
    print('Empatamos! Tente denovo.')
    
elif escolhaComputador == 'pedra' and escolhaUsuario == 'papel':
    print(f'Você ganhou de mim! Eu joguei {escolhaComputador}.')
    
elif escolhaComputador == 'pedra' and escolhaUsuario == 'tesoura':
    print(f'Você perdeu para mim! Eu joguei {escolhaComputador}.')
    
elif escolhaComputador == 'papel' and escolhaUsuario == 'pedra':
    print(f'Você perdeu para mim! Eu joguei {escolhaComputador}.')
    
elif escolhaComputador == 'papel' and escolhaUsuario == 'tesoura':
    print(f'Você ganhou de mim! Eu joguei {escolhaComputador}.')
    
elif escolhaComputador == 'tesoura' and escolhaUsuario == 'pedra':
    print(f'Você ganhou de mim! Eu joguei {escolhaComputador}.')
    
elif escolhaComputador == 'tesoura' and escolhaUsuario == 'papel':
    print(f'Você perdeu para mim! Eu joguei {escolhaComputador}.')