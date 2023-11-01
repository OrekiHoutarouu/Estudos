import Moeda

preco = float(input('Digite um valor: R$'))
porcentagemMais = float(input('Quantos porcentos deseja aumentar? '))
porcentagemMenos = float(input('Quantos porcentos deseja diminuir? '))

print('='*50)

print(f'O dobro de {(preco)} é {(Moeda.dobro(preco, True))}')
print(f'A metade de {(preco)} é {(Moeda.metade(preco, True))}')
print(f'Aumentando {porcentagemMais}% de {(preco)}, temos {(Moeda.aumentar(preco, porcentagemMais))}')
print(f'Diminuindo {porcentagemMenos}% de {(preco)}, temos {(Moeda.diminuir(preco, porcentagemMenos))}')