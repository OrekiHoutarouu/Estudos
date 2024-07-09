import Moeda

numero = float(input('Digite um valor: '))
porcentagemMais = float(input('Quantos porcentos deseja aumentar? '))
porcentagemMenos = float(input('Quantos porcentos deseja diminuir? '))

print('='*50)

print(f'O dobro de {numero} é {Moeda.dobro(numero)}')
print(f'A metade de {numero} é {Moeda.metade(numero)}')
print(f'Aumentando {porcentagemMais}% de {numero}, temos {Moeda.aumentar(numero, porcentagemMais)}')
print(f'Diminuindo {porcentagemMenos}% de {numero}, temos {Moeda.diminuir(numero, porcentagemMenos)}')