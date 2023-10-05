from random import randint
contadorVitorias = 0

print('='*50)
print('PAR OU ÍMPAR'.center(50))
print('='*50)

while True:
    jogadaComputador = randint(1,10)

    parOuImparUsuario = str(input('Par ou ímpar? [P/I]: ')).strip().upper()
    chuteUsuario = int(input('Escolha um número entre 0 e 10: '))

    if (chuteUsuario + jogadaComputador) % 2 == 0:
        print('='*50)
        print(f'Você jogou {chuteUsuario} e o computador jogou {jogadaComputador}, o total foi de {chuteUsuario + jogadaComputador}, então deu...\nPAR!')
        
        if parOuImparUsuario == "P":
            print('Você ganhou de mim! Vamos jogar denovo.')
            print('='*50)
            contadorVitorias += 1

        else:
            print('Você perdeu para mim! HAHAHA!')
            break
        
        
    else:
        print('='*50)
        print(f'Voçê jogou {chuteUsuario} e o computador jogou {jogadaComputador}, o total foi de {chuteUsuario + jogadaComputador}, então deu...\nÍMPAR!')
        
        if parOuImparUsuario == "I":
            print('Você ganhou de mim! Vamos jogar denovo.')
            print('-'*20)
            contadorVitorias += 1
        
        else:
            print('Você perdeu para mim! HAHAHA!')
            break
print(f'Você ganhou de mim {contadorVitorias} vez(es)!')