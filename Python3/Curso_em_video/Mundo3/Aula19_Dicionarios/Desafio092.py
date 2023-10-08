from datetime import datetime

dadosDoTrabalhador = {}

dadosDoTrabalhador['Nome'] = str(input('Nome: ')).strip()
dadosDoTrabalhador['Nascimento'] = int(input('Ano de nascimento: '))
dadosDoTrabalhador['Idade'] = datetime.now().year - dadosDoTrabalhador['Nascimento']
del(dadosDoTrabalhador['Nascimento'])
dadosDoTrabalhador['CTPS'] = int(input('Carteira de Trabalho (Digite 0 se não tem): '))

if dadosDoTrabalhador['CTPS'] != 0:
    dadosDoTrabalhador['Ano de Contratação'] = int(input('Ano de Contratação: '))
    dadosDoTrabalhador['Salário'] = float(input('Salário: '))
    dadosDoTrabalhador['Idade de aposentadoria'] = dadosDoTrabalhador['Idade'] + ((dadosDoTrabalhador['Ano de Contratação'] + 35) - datetime.now().year)

print('='*60)

for chave, valor in dadosDoTrabalhador.items():
    print(f'{chave} tem o valor {valor}')