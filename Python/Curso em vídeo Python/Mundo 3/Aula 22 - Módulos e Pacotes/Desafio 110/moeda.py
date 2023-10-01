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
    print(f'{"RESUMO DOS VALORES":>25}')
    print('='*33)
    
    print(f'Preço analisado: {moeda(preço):>13}')
    print(f'Dobro do preço: {dobro(preço, True):>15}')
    print(f'Metade do preço: {metade(preço, True):>13}')
    print(f'{porcentagemMais}% de aumento: {aumentar(preço, porcentagemMais, True):>14}')
    print(f'{porcentagemMenos}% de redução: {diminuir(preço, porcentagemMenos, True):>14}')