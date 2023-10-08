from random import randint
sequencia = randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10)

print('A sequência gerada foi: ', end='')
for contador in sequencia:
    print(f'{contador}', end=' ')
    
print(f'\nO maior número gerado foi {max(sequencia)} e o menor número gerado foi {min(sequencia)}.')