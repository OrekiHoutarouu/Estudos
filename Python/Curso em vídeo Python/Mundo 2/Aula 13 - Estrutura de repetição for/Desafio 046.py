from time import sleep
from emoji import emojize 

print('='*50)
print('CONTAGEM PARA ESTOURO DE FOGOS DE ARTIFÍCIO'.center(50))
print('='*50)

for contador in range (10,0, -1):
    sleep(1)
    print(contador)

print('='*50)
print(f'{emojize(":fireworks:")} FELIZ ANO NOVO {emojize(":fireworks:")}'.center(50))
print('='*50)