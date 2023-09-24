n = int(input('Digite um número para saber seu fatorial: '))
c = n
f = 1
while c > 0:
    print(f'{c}',end='')
    if c != 1:
        print(' x ',end='')
    f *= c
    c -= 1
print(f' = {f}')