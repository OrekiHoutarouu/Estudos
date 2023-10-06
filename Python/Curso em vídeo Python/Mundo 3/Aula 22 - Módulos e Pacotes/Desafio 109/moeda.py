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