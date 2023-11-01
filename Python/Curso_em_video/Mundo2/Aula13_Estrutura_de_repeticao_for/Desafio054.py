from datetime import datetime
anoAtual = datetime.today().year

maiorDeIdade = menorDeIdade = 0

for contador in range(1,8):
    anoNascimento = int(input(f'Digite o ano de nascimento da {contador}° pessoa: '))
    
    if anoAtual - anoNascimento > 18:
        maiorDeIdade += 1
        
    else:
        menorDeIdade += 1
        
print(f'Existem {maiorDeIdade} pessoa(s) maior(es) de idade, e {menorDeIdade} pessoa(s) menor(es) de idade na lista.')