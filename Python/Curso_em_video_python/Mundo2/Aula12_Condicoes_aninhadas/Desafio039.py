from datetime import datetime

anoAtual = datetime.today().year

anoDeNascimento = int(input('Digite seu ano de nascimento: '))

idade = anoAtual - anoDeNascimento

if idade < 18:
    print(f'Você ainda está muito novo para se alistar no exército, ainda faltam {18 - idade} ano(s).')
    
elif idade == 18:
    print(f'Você deve se alistar no exército esse ano, acesse o site alistamento.eb.mil.br e se aliste!') 
       
else:
    print(f'Você está muito velho para se alistar no exército, já se passaram {idade - 18} ano(s) da data certa.')    