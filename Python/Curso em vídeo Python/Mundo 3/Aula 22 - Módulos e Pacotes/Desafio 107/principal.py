import moeda

número = float(input('Digite um valor: '))
porcentagemMais = float(input('Quantos porcentos deseja aumentar? '))
porcentagemMenos = float(input('Quantos porcentos deseja diminuir? '))

print('='*50)

print(f'O dobro de {número} é {moeda.dobro(número)}')
print(f'A metade de {número} é {moeda.metade(número)}')
print(f'Aumentando {porcentagemMais}% de {número}, temos {moeda.aumentar(número, porcentagemMais)}')
print(f'Diminuindo {porcentagemMenos}% de {número}, temos {moeda.diminuir(número, porcentagemMenos)}')