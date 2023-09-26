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