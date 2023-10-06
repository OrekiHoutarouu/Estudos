from random import randint

numeros = []

def sorteia():
    print('Sorteando 5 valores aleatórios:', end=' ')
   
    for aleatorios in range(0,5):
        numeros.append(randint(0,10))
        
    for aleatorios in numeros:
        print(f'{aleatorios}', end='')
        
def somaPar(numeros):
    numerosPares = 0
    print('\nSomando os valores pares de ',end ='')
    
    for valores in numeros:
        print(f'{valores}', end=' ')
        
    print('...')
    
    for valores in numeros:
        if valores % 2 == 0:
            numerosPares += valores
            
    print(f'{numerosPares}')
    
    
sorteia()
somaPar(numeros)