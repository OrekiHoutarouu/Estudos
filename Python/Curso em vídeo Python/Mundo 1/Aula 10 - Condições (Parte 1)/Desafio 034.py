salário = float(input('Digite o salário do funcionário: '))

if salário > 1250:
    print(f'O salário desse funcionário com aumento de 10% ficou por R${(salário + (salário * (10 / 100))):.2f}.')
    
else:
    print(f'O salário desse funcionário com aumento de 15% ficou por R${(salário + (salário * (15 / 100))):.2f}.')    