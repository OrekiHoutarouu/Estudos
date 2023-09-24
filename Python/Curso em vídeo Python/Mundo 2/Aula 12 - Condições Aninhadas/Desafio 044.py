pn = float(input('Digite o preço normal do produto: R$'))
cp = int(input('Digite a condição de pagamento, digite 1 para à vista e 2 para parcelado: '))
if cp == 1:
    av = int(input('Digite 1 para pagamento no dinheiro, 2 para pagamento no cartão e 3 para pagamento em cheque: '))
    if av == 1 or av == 3:
        print(f'O preço do produto vai ser de R${pn-(pn*(10/100)):.2f}.') 
    elif av == 2:
        print(f'O preço do produto vai ser de R${pn-(pn*(5/100)):.2f}.')
if cp == 2:
    p = int(input('Digite 1 para parcelado em 2x e 2 para 3x ou mais: '))
    if p == 1:
        print(f'O preço do produto vai ser de R${pn:.2f}\nCom 2 parcelas de {pn/2:.2f}.')
    elif p == 2:
        qp = int(input(f'Em quantas vezes deseja parcelar o produto? '))
        print(f'O preço do produto vai ser de R${pn+(pn*(20/100))}\nCom {qp} parcelas de R${(pn+(pn*(20/100)))/qp}.')