pt = int(input('Digite o primeiro termo da Progressão Aritimética: '))
r = int(input('Digite a razão da Progressão Aritimética: '))
n = qt = 1
while n < 11:
    print(f'O {n}° termo dessa Progressão Aritimética é {pt}')
    pt += r
    n += 1
while qt != 0:
    qt = int(input('Quantos termos a mais deseja adicionar a essa Progressão Aritimética? Digite 0 caso não queira adicionar nenhum: '))
    for c in range(qt):
        print(f'O {n}° termo dessa Progressão Aritimética é {pt}')
        n += 1
        pt += r