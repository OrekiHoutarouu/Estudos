s = 0
for c in range(1, 7):
    ns = int(input('Digite um valor: '))
    if ns % 2 == 0:
        s = s + ns
print(f'A soma de todos os núemros pares digitados foi de {s} (números ímpares não foram considerados)')