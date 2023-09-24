from random import randint

números = []

def sorteia():
    print('Sorteando 5 valores aleatórios:', end=' ')
   
    for aleatórios in range(0,5):
        números.append(randint(0,10))
        
    for aleatórios in números:
        print(f'{aleatórios}', end='')
        
def somaPar(números):
    númerosPares = 0
    print('\nSomando os valores pares de ',end ='')
    
    for valores in números:
        print(f'{valores}', end=' ')
        
    print('...')
    
    for valores in números:
        if valores % 2 == 0:
            númerosPares += valores
            
    print(f'{númerosPares}')
    
    
sorteia()
somaPar(números)