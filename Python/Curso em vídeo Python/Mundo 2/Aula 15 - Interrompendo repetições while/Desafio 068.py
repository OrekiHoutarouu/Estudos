from random import randint
contadorVitórias = 0
print(f'VAMOS JOGAR PAR OU ÍMPAR\n{"-"*24}')

while True:
    jogadaComputador = randint(1,10)

    parOuÍmparUsuário = str(input('Par ou ímpar? [P/I]: ')).strip().upper()
    jogadaUsuário = int(input('Escolha um número entre 0 e 10: '))

    if (jogadaUsuário + jogadaComputador) % 2 == 0:
        print('-'*20)
        print(f'Você jogou {jogadaUsuário} e o computador jogou {jogadaComputador}, o total foi de {jogadaUsuário + jogadaComputador}, então deu...\nPAR!')
        if parOuÍmparUsuário == "P":
            print('Você ganhou de mim! Vamos jogar denovo.')
            print('-'*20)
            contadorVitórias += 1

        else:
            print('Você perdeu para mim! HAHAHA!')
            break
    else:
        print('-'*20)
        print(f'Voçê jogou {jogadaUsuário} e o computador jogou {jogadaComputador}, o total foi de {jogadaUsuário + jogadaComputador}, então deu...\nÍMPAR!')
        if parOuÍmparUsuário == "I":
            print('Você ganhou de mim! Vamos jogar denovo.')
            print('-'*20)
            contadorVitórias += 1
        
        else:
            print('Você perdeu para mim! HAHAHA!')
            break
print(f'Você ganhou de mim {contadorVitórias} vez(es)!')