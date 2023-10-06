precoNormal = float(input('Digite o preço normal do produto: R$'))
condicaoPagamento = int(input('Digite a condição de pagamento, digite 1 para à vista e 2 para parcelado: '))

if condicaoPagamento == 1:
    aVista = int(input('Digite 1 para pagamento no dinheiro, 2 para pagamento no cartão e 3 para pagamento em cheque: '))
    
    if aVista == 1 or aVista == 3:
        print(f'O preço do produto vai ser de R${precoNormal-(precoNormal*(10/100)):.2f}.') 
        
    elif aVista == 2:
        print(f'O preço do produto vai ser de R${precoNormal-(precoNormal*(5/100)):.2f}.')
        
        
if condicaoPagamento == 2:
    parcelado = int(input('Digite 1 para parcelado em 2x e 2 para 3x ou mais: '))
    
    if parcelado == 1:
        print(f'O preço do produto vai ser de R${precoNormal:.2f}\nCom 2 parcelas de {precoNormal/2:.2f}.')
        
    elif parcelado == 2:
        quantidadeParcelas = int(input(f'Em quantas vezes deseja parcelar o produto? '))
        
        print(f'O preço do produto vai ser de R${precoNormal+(precoNormal*(20/100)):.2f}\nCom {quantidadeParcelas} parcelas de R${(precoNormal+(precoNormal*(20/100)))/quantidadeParcelas:.2f}.')