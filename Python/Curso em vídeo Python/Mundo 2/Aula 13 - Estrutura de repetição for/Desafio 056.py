idadeMedia = 0
idadeHomemVelho = 0
nomeHomemVelho = ''
numeroMulheresMaiorDeVinte = 0

for contador in range(1, 5):
    print(f'{"-"*5} {contador}° Pessoa {"-"*5}')
    
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M ou F): ')).upper().strip()
    idadeMedia += idade
    
    if contador == 1 and sexo == 'M':
        idadeHomemVelho = idade
        nomeHomemVelho = nome
        
    if sexo == 'M' and idade > idadeHomemVelho:
        idadeHomemVelho = idade
        nomeHomemVelho = nome
        
    if sexo == 'F' and idade < 20:
        numeroMulheresMaiorDeVinte += 1
        
print(f'A média de idade das pessoas digitadas é de: {(idadeMedia)/4:.1f}.')
print(f'O nome do homem mais velho da lista é {nomeHomemVelho} e ele tem {idadeHomemVelho} ano(s).')
print(f'Existem {numeroMulheresMaiorDeVinte} mulher(es) que tem menos de 20 anos nessa lista.')