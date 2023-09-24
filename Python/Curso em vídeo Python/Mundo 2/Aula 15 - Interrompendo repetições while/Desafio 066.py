contador = soma = 0
while True:
    número = int(input(f'Digite o {contador + 1}° número (999 para finalizar): '))
    if número == 999:
        break
    soma += número
    contador += 1
print(f'Você digitou {contador} números e a soma entre eles é igual a {soma}.')