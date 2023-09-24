s = float(input('Digite o salário do funcionário: '))
if s > 1250:
    print(f'O salário desse funcionário com aumento de 10% ficou por R${(s+(s*(10/100))):.2f}')
else:
    print(f'O salário desse funcionário com aumento de 15% ficou por R${(s+(s*(15/100))):.2f}')    