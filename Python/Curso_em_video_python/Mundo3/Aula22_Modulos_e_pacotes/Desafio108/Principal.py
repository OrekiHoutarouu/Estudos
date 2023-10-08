import Moeda

preco = float(input('Digite um valor: R$'))
porcentagemMais = float(input('Quantos porcentos deseja aumentar? '))
porcentagemMenos = float(input('Quantos porcentos deseja diminuir? '))

print('='*50)

print(f'O dobro de {Moeda.moeda(preco)} é {Moeda.moeda(Moeda.dobro(preco))}')
print(f'A metade de {Moeda.moeda(preco)} é {Moeda.moeda(Moeda.metade(preco))}')
print(f'Aumentando {porcentagemMais}% de {Moeda.moeda(preco)}, temos {Moeda.moeda(Moeda.aumentar(preco, porcentagemMais))}')
print(f'Diminuindo {porcentagemMenos}% de {Moeda.moeda(preco)}, temos {Moeda.moeda(Moeda.diminuir(preco, porcentagemMenos))}')