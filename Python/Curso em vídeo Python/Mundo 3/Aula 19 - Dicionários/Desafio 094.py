pessoa = {}
listaDePessoas = []
somaDasIdades = 0

while True:
    pessoa['Nome'] = str(input('Nome: ')).strip()

    while True:
        pessoa['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
        
        if pessoa['Sexo'] in 'MF':
            break
        
        else:
            print('Valor inválido, digite apenas M ou F.')
            
    pessoa['Idade'] = int(input('Idade: '))
    somaDasIdades += pessoa['Idade']
    
    listaDePessoas.append(pessoa.copy())
    
    while True:
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()
        
        if continuar in 'SN':
            break
        
        else:
            print('Valor inválido, digite apenas S ou N.')
            
    if continuar in 'N':
        break
    
print('='*60)

print(f'Ao todo, temos {len(listaDePessoas)} pessoa(s) cadastrada(s).')
print(f'A média de idade do(a)(s) cadastrado(a)(s) é de {somaDasIdades / len(listaDePessoas):.2f}')
print('A(s) mulher(es) cadastrada(s) foram ', end='')

for mulheres in listaDePessoas:
    if mulheres['Sexo'] in 'F':
        print(f'{mulheres["Nome"]}...', end='')

print('\nA(s) pessoa(s) acima da média de idade foi(ram):')

for acimaDaMédia in listaDePessoas:
    if acimaDaMédia['Idade'] > (somaDasIdades / len(listaDePessoas)):
        for chave, valor in acimaDaMédia.items():
            print(f'{chave} = {valor}; ', end='')
        print()