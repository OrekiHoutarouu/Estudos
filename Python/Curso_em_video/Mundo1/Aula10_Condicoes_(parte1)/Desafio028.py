from random import randint
from emoji import emojize

númeroAleatório = randint(0, 5)

chute = int(input('Vou pensar num número entre 0 e 5, tente adivinhar: '))

if chute == númeroAleatório:
    print(f'Parabéns você acertou o número! {emojize(":fireworks:")}')
    
else:
     print(f'Que pena, você errou o número {emojize(":pensive_face:")}')  
     print(f'O número certo era {númeroAleatório}.')   