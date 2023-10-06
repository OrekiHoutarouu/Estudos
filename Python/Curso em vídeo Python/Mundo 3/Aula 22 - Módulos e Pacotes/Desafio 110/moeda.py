def dobro(preco = 0, formatar = False):
    preco *= 2
    
    if formatar == False:
        return preco
    
    else:
        return moeda(preco)


def metade(preco = 0, formatar = False):
    preco /= 2
    
    if formatar == False:
        return preco
    
    else:
        return moeda(preco)


def aumentar(preco = 0, porcentagem = 0, formatar = False):
    preco = preco + (preco * (porcentagem / 100))
    
    if formatar == False:
        return preco
    
    else:
        return moeda(preco)


def diminuir(preco = 0, porcentagem = 0, formatar = False):
    preco = preco - (preco * (porcentagem / 100))
    
    if formatar == False:
        return preco
    
    else:
        return moeda(preco)


def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')

def resumo(preco = 0, porcentagemMais = 0, porcentagemMenos = 0):
    print('='*33)
    print('RESUMO DOS VALORES'.center(33))
    print('='*33)
    
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preco: \t{dobro(preco, True)}')
    print(f'Metade do preco: \t{metade(preco, True)}')
    print(f'{porcentagemMais}% de aumento: \t{aumentar(preco, porcentagemMais, True)}')
    print(f'{porcentagemMenos}% de redução: \t{diminuir(preco, porcentagemMenos, True)}')