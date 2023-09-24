n1 = float(input('Digite a primeira nota do  aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
m = (n1+n2)/2
if m < 5:
    print('Aluno reprovado, pois sua média está abaixo de 5.')
elif m >= 7:
    print('Aluno aprovado, pois sua média está acima de 7.')
else:
    print('Aluno em recuperação, pois sua média está entre 5 e 6,9.')        