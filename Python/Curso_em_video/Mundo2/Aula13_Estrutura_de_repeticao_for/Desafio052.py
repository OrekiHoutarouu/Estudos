numero = int(input('Digite um número pra saber se ele é primo: '))
total = 0

for contador in range(1, numero+1):
    if numero % contador == 0:
        total += 1
        
if total == 2:
     print('O número digitado é primo.')
     
else:
    print('O número digitado não é primo.')