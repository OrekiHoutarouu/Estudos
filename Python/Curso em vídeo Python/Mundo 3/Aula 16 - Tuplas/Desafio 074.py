from random import randint
sequência = randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10)

print('A sequência gerada foi: ',end='')
for c in sequência:
    print(f'{c}',end=' ')
    
print(f'\nO maior número gerado foi {max(sequência)} e o menor número gerado foi {min(sequência)}')