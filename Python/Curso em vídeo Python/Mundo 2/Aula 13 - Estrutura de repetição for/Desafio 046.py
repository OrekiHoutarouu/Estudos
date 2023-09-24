from time import sleep
from emoji import emojize 
print('{} CONTAGEM PARA ESTOURO DE FOGOS DE ARTIFÍCIO {}'.format('='*20,'='*20))
for c in range (10,0, -1):
    sleep(1)
    print(c)
print('{}{} FELIZ ANO NOVO {}{}'.format('='*20, emojize(":fireworks:"), emojize(":fireworks:"), '='*20))