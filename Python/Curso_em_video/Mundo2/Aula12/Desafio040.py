numero1 = float(input('Digite a primeira nota do  aluno: '))
numero2 = float(input('Digite a segunda nota do aluno: '))

media = (numero1 + numero2) / 2

if media < 5:
    print('Aluno reprovado, pois sua média está abaixo de 5.')
    
elif media >= 7:
    print('Aluno aprovado, pois sua média está acima de 7.')
    
else:
    print('Aluno em recuperação, pois sua média está entre 5 e 6,9.')        