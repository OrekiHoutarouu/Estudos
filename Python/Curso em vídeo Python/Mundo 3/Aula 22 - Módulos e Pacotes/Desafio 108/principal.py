import moeda

número = float(input('Digite um valor: R$'))
porcentagemMais = float(input('Quantos porcentos deseja aumentar? '))
porcentagemMenos = float(input('Quantos porcentos deseja diminuir? '))

print('='*50)

print(f'O dobro de R${número} é R${moeda.dobro(número):.2f}')
print(f'A metade de R${número} é R${moeda.metade(número):.2f}')
print(f'Aumentando {porcentagemMais}% de R${número}, temos R${moeda.aumentar(número, porcentagemMais):.2f}')
print(f'Diminuindo {porcentagemMenos}% de R${número}, temos R${moeda.diminuir(número, porcentagemMenos):.2f}')