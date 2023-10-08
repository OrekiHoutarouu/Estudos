from Utilidades_CeV import Moeda, Dado

preco = Dado.leiaDinheiro(('Digite um valor: R$'))
Moeda.resumo(preco, 20, 12)