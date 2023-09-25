from time import sleep

def contador(início, fim, passo):
    if passo < 0:
        passo *= -1
        
    if passo == 0:
        passo = 1
        
    print('=' * 50)
    print(f'Contagem de {início}, até {fim}, de {passo} em {passo}:')
        
    if fim > início:
        for contagem in range(início, fim + 1, passo):
            print(f'{contagem}', end=' ')
            sleep(0.3)
        print()
        
    else:
        for contagem in range(início, fim - 1, -passo):
            print(f'{contagem}', end=' ')
            sleep(0.3)
        print()
        
        
contador(1, 10, 1)
contador(10, 0, 2)
    
print('='*50)

início = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(início, fim, passo)