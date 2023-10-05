from random import randint
numeroAleatorio = randint(0,10)
numeroChutesUsuario = 0

print('Eu vou pensar em um número aleatório entre 0 e 10, vá chutando números até acertar qual número eu pensei!')

chuteUsuario = int(input('Digite aqui o seu chute: '))
numeroChutesUsuario += 1

while chuteUsuario != numeroAleatorio:
    chuteUsuario = int(input('Você errou, tente denovo com outro número: '))
    numeroChutesUsuario += 1
    
if numeroChutesUsuario == 1:
    print('Uau, na primeira tentativa você acertou, parabéns!')
    
elif numeroChutesUsuario == 2:
    print('Quase de primeira né? mas pelo ao menos foi na segunda tentativa, parabéns!')
    
else:
    print(f'Finalmente você acertou, você chutou um total de {numeroChutesUsuario} números até acertar, parabéns!')