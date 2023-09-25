def dobro(número):
    número *= 2
    return número


def metade(número):
    número /= 2
    return número


def aumentar(número, porcentagem):
    número = número + (número * (porcentagem / 100))
    return número


def diminuir(número, porcentagem):
    número = número - (número * (porcentagem / 100))
    return número