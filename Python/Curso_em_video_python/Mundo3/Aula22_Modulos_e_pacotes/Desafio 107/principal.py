import moeda

numero = float(input('Digite um valor: '))
porcentagemMais = float(input('Quantos porcentos deseja aumentar? '))
porcentagemMenos = float(input('Quantos porcentos deseja diminuir? '))

print('='*50)

print(f'O dobro de {numero} é {moeda.dobro(numero)}')
print(f'A metade de {numero} é {moeda.metade(numero)}')
print(f'Aumentando {porcentagemMais}% de {numero}, temos {moeda.aumentar(numero, porcentagemMais)}')
print(f'Diminuindo {porcentagemMenos}% de {numero}, temos {moeda.diminuir(numero, porcentagemMenos)}')