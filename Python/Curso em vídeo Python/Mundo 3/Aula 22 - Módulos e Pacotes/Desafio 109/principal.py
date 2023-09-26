import moeda

preço = float(input('Digite um valor: R$'))
porcentagemMais = float(input('Quantos porcentos deseja aumentar? '))
porcentagemMenos = float(input('Quantos porcentos deseja diminuir? '))

print('='*50)

print(f'O dobro de {(preço)} é {(moeda.dobro(preço, True))}')
print(f'A metade de {(preço)} é {(moeda.metade(preço, True))}')
print(f'Aumentando {porcentagemMais}% de {(preço)}, temos {(moeda.aumentar(preço, porcentagemMais))}')
print(f'Diminuindo {porcentagemMenos}% de {(preço)}, temos {(moeda.diminuir(preço, porcentagemMenos))}')