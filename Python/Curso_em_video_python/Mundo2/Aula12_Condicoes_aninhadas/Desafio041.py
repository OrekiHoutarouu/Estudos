from datetime import datetime
anoAtual = datetime.today().year

anoNascimento = int(input('Digite a data de nascimento do atleta para mostrar sua categoria: '))

idade = anoAtual - anoNascimento

if idade <= 9:
    print('Atleta Mirim.')
    
elif (idade > 9) and (idade <= 14):
    print('Atleta Infantil.')
    
elif (idade > 14) and (idade <= 19):
    print('Atleta Junior.')    
    
elif (idade > 19) and (idade <=20):
    print('Atleta Sênior.')
    
else:
    print('Atleta Master.')    