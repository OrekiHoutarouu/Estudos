soma = 0

for c in range(1, 7):
    numero = int(input('Digite um valor: '))
    
    if numero % 2 == 0:
        soma += numero
        
print(f'A soma de todos os números pares digitados foi de {soma}.')