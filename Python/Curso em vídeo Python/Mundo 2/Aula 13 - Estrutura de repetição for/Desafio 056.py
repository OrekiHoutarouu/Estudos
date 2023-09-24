ida = 0
mh = 0
nhv = ''
mn = 0
for c in range(1, 5):
    print(f'{"-"*5} {c}° Pessoa {"-"*5}')
    n = str(input('Nome: ')).strip()
    i = int(input('Idade: '))
    s = str(input('Sexo (M ou F): ')).upper().strip()
    ida += i
    if c == 1 and s == 'M':
        mh = i
        nhv = n
    if s == 'M' and i > mh:
        mh = i
        nhv = n
    if s == 'F' and i < 20:
        mn += 1
print(f'A média de idade das pessoas digitadas é de: {(ida)/4:.1f}')
print(f'O nome do homem mais velho da lista é {nhv} e ele tem {mh} ano(s).')
print(f'Existem {mn} mulher(es) que tem menos de 20 anos nessa lista.')