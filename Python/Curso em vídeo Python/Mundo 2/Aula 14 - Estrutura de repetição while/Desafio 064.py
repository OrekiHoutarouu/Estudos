numero = contador = soma = 0

while numero != 999:
    numero = int(input('Digite um número para saber sua soma com o próximo número, digite 999 para encerrar o programa: '))
    soma += numero
    contador += 1
    
print(f'Você digitou {contador - 1} números e a soma entre eles é de {soma - 999}.')