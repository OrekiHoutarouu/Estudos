def dobro(preco):
    preco *= 2
    return preco


def metade(preco):
    preco /= 2
    return preco


def aumentar(preco, porcentagem):
    preco = preco + (preco * (porcentagem / 100))
    return preco


def diminuir(preco, porcentagem):
    preco = preco - (preco * (porcentagem / 100))
    return preco