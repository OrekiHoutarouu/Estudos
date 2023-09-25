def dobro(preço):
    preço *= 2
    return preço


def metade(preço):
    preço /= 2
    return preço


def aumentar(preço, porcentagem):
    preço = preço + (preço * (porcentagem / 100))
    return preço


def diminuir(preço, porcentagem):
    preço = preço - (preço * (porcentagem / 100))
    return preço