a = int(input('Digite um ano para descobrir se ele é bissexto: '))
if a%4==0 and a %100!=0 or a%400==0:
    print('O ano digitado é bissexto!')
else:
    print('O ano digitado não é bissexto!')    