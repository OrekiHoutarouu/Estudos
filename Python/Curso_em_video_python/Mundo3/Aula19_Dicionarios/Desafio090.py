aluno = {}

aluno['Nome'] = str(input('Nome: ')).strip()
aluno['Média'] = float(input('Média: '))

if aluno['Média'] >= 6:
    aluno['Situação'] = 'Aprovado'
    
else:
    aluno['Situação'] = 'Reprovado'
 
for chave, valor in aluno.items():   
    print(f'{chave} é igual a {valor}')