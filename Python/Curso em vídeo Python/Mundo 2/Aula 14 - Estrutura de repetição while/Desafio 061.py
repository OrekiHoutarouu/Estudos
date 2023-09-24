pt = int(input('Digite o primeiro termo da Progressão aritimética: '))
r = int(input('Digite a razão da progressão aritimética: '))
n = 1
while n < 11:
    print(f'O {n}° termo dessa progressão aritimética é {pt}')
    pt += r
    n += 1