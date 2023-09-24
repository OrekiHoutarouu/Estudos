v = float(input('Digite o valor da casa: R$'))
s = float(input('Digite o salário: R$'))
a = int(input('Digite em quantos anos será paga a casa: '))
p = v/(a*12)
if p > s*0.30:
    print('O empréstimo foi negado pois a prestação mensal ultrapassa o salário em 30% ou mais.')
else:
    print(f'O empréstimo foi aceito! O comprador terá que pagar {p:.2f} por mês')