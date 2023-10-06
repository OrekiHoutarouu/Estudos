import moeda

preco = float(input('Digite um valor: R$'))
porcentagemMais = float(input('Quantos porcentos deseja aumentar? '))
porcentagemMenos = float(input('Quantos porcentos deseja diminuir? '))

print('='*50)

print(f'O dobro de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}')
print(f'A metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}')
print(f'Aumentando {porcentagemMais}% de {moeda.moeda(preco)}, temos {moeda.moeda(moeda.aumentar(preco, porcentagemMais))}')
print(f'Diminuindo {porcentagemMenos}% de {moeda.moeda(preco)}, temos {moeda.moeda(moeda.diminuir(preco, porcentagemMenos))}')