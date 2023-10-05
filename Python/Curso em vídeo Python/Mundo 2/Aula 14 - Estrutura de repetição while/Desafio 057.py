sexo = str(input('Digite seu sexo: M para masculino e F para feminino: ')).upper().strip()[0]

while sexo not in 'MF':
    sexo = str(input('Valor digitado inválido. Digite novamente: M para masculino e F para feminino: ')).upper().strip()[0]
    
print('Sexo cadastrado com sucesso!')