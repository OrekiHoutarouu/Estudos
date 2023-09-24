p = float(input('Digite seu peso: '))
a = float(input('Digite sua altura: '))
imc = p / (a**2)
if imc < 18.5:
    print('Você está abaixo do peso ideal, tente fazer uma dieta de superávit calórico!')
elif (imc > 18.5) and (imc < 25):
    print('Você está com o peso ideal, mantenha-se assim!')
elif (imc > 25) and (imc < 30):
    print('Você está com sobrepeso, tente fazer uma dieta de déficit calórico e pratique atividades físicas de alta itensidade!')  
elif (imc > 30) and (imc < 40):
    print('Você está obeso, faça uma dieta de déficit calórico acompanhada por nutricionista, faça uma reeducação alimentar e pratique atividades físicas de alta itensidade com acompanhamento de um profissional!') 
else:
    print('Você está com obesidade mórbida, procure um médico imediatamente, o profissional com certeza de ajudará a ficar mais saudável, pois você corre muitos riscos de saúde!')
print(f'seu IMC é de {imc:.1f}')