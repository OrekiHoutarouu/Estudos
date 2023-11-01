from time import sleep

def maior(*numeros):
    print('='*50)
    
    print(f'Analisando os valores', end=' ')
    
    for valores in numeros:
        print(f'{valores}', end=' ')
        sleep(0.3)
        
    print(f'\nForam informados {len(numeros)} valores.')
    
    if len(numeros) == 0:
        print('O maior valor informado foi 0')
        
    else:
        print(f'O maior valor informado foi {max(numeros)}.')
    
    
    
maior(2, 9, 4, 5, 7, 1)

maior(4, 7, 0)

maior(1, 2)

maior(6)

maior()