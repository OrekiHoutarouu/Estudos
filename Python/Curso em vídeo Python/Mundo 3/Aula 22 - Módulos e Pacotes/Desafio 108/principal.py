import moeda

preço = float(input('Digite um valor: R$'))
porcentagemMais = float(input('Quantos porcentos deseja aumentar? '))
porcentagemMenos = float(input('Quantos porcentos deseja diminuir? '))

print('='*50)

print(f'O dobro de {moeda.moeda(preço)} é {moeda.moeda(moeda.dobro(preço))}')
print(f'A metade de {moeda.moeda(preço)} é {moeda.moeda(moeda.metade(preço))}')
print(f'Aumentando {porcentagemMais}% de {moeda.moeda(preço)}, temos {moeda.moeda(moeda.aumentar(preço, porcentagemMais))}')
print(f'Diminuindo {porcentagemMenos}% de {moeda.moeda(preço)}, temos {moeda.moeda(moeda.diminuir(preço, porcentagemMenos))}')