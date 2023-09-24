from datetime import datetime
a = datetime.today().year
an = int(input('Digite seu ano de nascimento: '))
i = a - an
if i < 18:
    print(f'Você ainda está muito novo para se alistar no exército, ainda faltam {18 - i} ano(s).')
elif i == 18:
    print(f'Você deve se alistar no exército esse ano, acesse o site alistamento.eb.mil.br e se aliste!')    
else:
    print(f'Você está muito velho para se alistar no exército, já se passaram {i - 18} ano(s) da data certa.')    