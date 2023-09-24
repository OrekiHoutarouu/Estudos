n = int(input('Digite um número pra saber se ele é primo: '))
t = 0
for c in range(1, n+1):
    if n % c == 0:
        t += 1
if t == 2:
     print('O número digitado é primo.')
else:
    print('O número digitado não é primo.')