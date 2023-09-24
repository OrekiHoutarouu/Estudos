s = str(input('Digite seu sexo: M para masculino e F para feminino: ')).upper().strip()[0]
while s not in 'MF':
    s = str(input('Valor digitado inválido. Digite novamente: M para masculino e F para feminino: ')).upper().strip()[0]
print('Sexo cadastrado com sucesso!')