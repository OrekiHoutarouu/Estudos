from time import sleep

def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
        
    if passo == 0:
        passo = 1
        
    print('=' * 50)
    print(f'Contagem de {inicio}, até {fim}, de {passo} em {passo}:')
        
    if fim > inicio:
        for contagem in range(inicio, fim + 1, passo):
            print(f'{contagem}', end=' ')
            sleep(0.3)
        print()
        
    else:
        for contagem in range(inicio, fim - 1, -passo):
            print(f'{contagem}', end=' ')
            sleep(0.3)
        print()
        
        
contador(1, 10, 1)
contador(10, 0, 2)
    
print('='*50)

inicio = int(input('inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(inicio, fim, passo)