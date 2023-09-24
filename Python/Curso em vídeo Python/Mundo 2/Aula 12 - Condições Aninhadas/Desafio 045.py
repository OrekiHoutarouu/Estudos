from random import choice
o = ['pedra','papel' ,'tesoura' ]
c = choice(o)
p = str(input('Vamos jogar Jokenpô? Digite pedra, papel ou tesoura: ')).strip().lower()
if c == p:
    print('Empatamos! Tente denovo.')
elif c == 'pedra' and p == 'papel':
    print(f'Você ganhou de mim! Eu joguei {c}')
elif c == 'pedra' and p == 'tesoura':
    print(f'Você perdeu para mim! Eu joguei {c}')
elif c == 'papel' and p == 'pedra':
    print(f'Você perdeu para mim! Eu joguei {c}')
elif c == 'papel' and p == 'tesoura':
    print(f'Você ganhou de mim! Eu joguei {c}')
elif c == 'tesoura' and p == 'pedra':
    print(f'Você ganhou de mim! Eu joguei {c}')
elif c == 'tesoura' and p == 'papel':
    print(f'Você perdeu para mim! Eu joguei {c}')