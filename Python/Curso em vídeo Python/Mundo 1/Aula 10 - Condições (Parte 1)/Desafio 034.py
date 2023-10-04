salario = float(input('Digite o salário do funcionário: '))

if salario > 1250:
    print(f'O salário desse funcionário com aumento de 10% ficou por R${(salario + (salario * (10 / 100))):.2f}.')
    
else:
    print(f'O salário desse funcionário com aumento de 15% ficou por R${(salario + (salario * (15 / 100))):.2f}.')    