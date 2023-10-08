soma = 0

for contador in range(1, 501, 2):
    if contador % 3 == 0:
        soma += contador
        
print(f'A soma de todos os números ímpares, múltiplos de 3 e entre 1 e 500 é de {soma}.')