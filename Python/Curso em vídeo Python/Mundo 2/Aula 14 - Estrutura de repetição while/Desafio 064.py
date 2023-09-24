n = c = r = 0
while n != 999:
    n = int(input('Digite um número para saber sua soma com o próximo número, digite 999 para encerrar o programa: '))
    r += n
    c += 1
print(f'Você digitou {c - 1} números e a soma entre eles é de {r - 999}')