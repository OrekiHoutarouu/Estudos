print(f'{"-"*13} BANCO DO SAM {"-"*13}\nSÓ TEMOS NOTAS DE R$50, R$20, R$10 e R$1\n{"-"*40}')

valorSacado = int(input('Digite o valor a ser sacado: '))

total = valorSacado
cédulaAtual = 50
totalCédulas = 0

while True:
    if total >= cédulaAtual:
        total -= cédulaAtual
        totalCédulas += 1
    else:
        if totalCédulas > 0:
            print(f'Total de {totalCédulas} cédula(s) de R${cédulaAtual}')
        if cédulaAtual == 50:
            cédulaAtual = 20
        elif cédulaAtual == 20:
            cédulaAtual = 10
        elif cédulaAtual == 10:
            cédulaAtual = 1
        totalCédulas = 0
        if total == 0:
            break
print(f'{"-"*5} VOLTE SEMPRE AO BANCO DO SAM {"-"*5}')