número = int(input('Digite um número inteiro entre 0 e 9999: '))

unidade = número // 1 % 10
dezena = número // 10 % 10
centena = número // 100 % 10
milhar = número // 1000 % 10

print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')