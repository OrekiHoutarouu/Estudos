valor = float(input('Digite o valor da casa: R$'))
salário = float(input('Digite o salário: R$'))
anos = int(input('Digite em quantos anos será paga a casa: '))

preço = valor / (anos * 12)

if preço > salário * 0.30:
    print('O empréstimo foi negado pois a prestação mensal ultrapassa o salário em 30% ou mais.')
    
else:
    print(f'O empréstimo foi aceito! O comprador terá que pagar {preço:.2f} por mês.')