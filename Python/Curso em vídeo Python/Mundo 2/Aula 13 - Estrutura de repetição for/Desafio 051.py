pt = int(input('Digite o primeiro termo da Progressão Aritimética: '))
r = int(input('Digite a razão da Progressão Aritimética: '))
n = 1
for c in range(10):
    print(f'O {n}° termo dessa Progressão Aritimética é {pt}')
    pt += r
    n += 1