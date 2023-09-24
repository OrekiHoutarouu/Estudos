from random import randint
na = randint(0,10)
np = 0
print('Eu vou pensar em um número aleatório entre 0 e 10, vá chutando números até acertar qual número eu pensei!')
nc = int(input('Digite aqui o seu chute: '))
np += 1
while nc != na:
    nc = int(input('Você errou, tente denovo com outro número: '))
    np += 1
if np == 1:
    print('Uau, na primeira tentativa você acertou, parabéns!')
elif np == 2:
    print('Quase de primeira né? mas pelo ao menos foi na segunda tentativa, parabéns!')
else:
    print(f'Finalmente você acertou, você chutou um total de {np} números até acertar, parabéns!')