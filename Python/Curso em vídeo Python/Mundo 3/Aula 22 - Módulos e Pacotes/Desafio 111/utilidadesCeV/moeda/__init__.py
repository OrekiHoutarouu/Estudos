def dobro(preço = 0, formatar = False):
    preço *= 2
    
    if formatar == False:
        return preço
    
    else:
        return moeda(preço)


def metade(preço = 0, formatar = False):
    preço /= 2
    
    if formatar == False:
        return preço
    
    else:
        return moeda(preço)


def aumentar(preço = 0, porcentagem = 0, formatar = False):
    preço = preço + (preço * (porcentagem / 100))
    
    if formatar == False:
        return preço
    
    else:
        return moeda(preço)


def diminuir(preço = 0, porcentagem = 0, formatar = False):
    preço = preço - (preço * (porcentagem / 100))
    
    if formatar == False:
        return preço
    
    else:
        return moeda(preço)


def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')

def resumo(preço = 0, porcentagemMais = 0, porcentagemMenos = 0):
    print('='*33)
    print('RESUMO DOS VALORES'.center(33))
    print('='*33)
    
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{porcentagemMais}% de aumento: \t{aumentar(preço, porcentagemMais, True)}')
    print(f'{porcentagemMenos}% de redução: \t{diminuir(preço, porcentagemMenos, True)}')