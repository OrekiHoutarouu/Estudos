from datetime import datetime
a = datetime.today().year
an = int(input('Digite a data de nascimento do atleta para mostrar sua categoria: '))
i = a - an
if i <= 9:
    print('Atleta Mirim.')
elif (i > 9) and (i <= 14):
    print('Atleta Infantil')
elif (i > 14) and (i <= 19):
    print('Atleta Junior')    
elif (i > 19) and (i <=20):
    print('Atleta Sênior')
else:
    print('Atleta Master')    