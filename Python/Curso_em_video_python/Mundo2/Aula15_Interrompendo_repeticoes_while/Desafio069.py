print('='*50)
print('ANALISADOR DE DADOS'.center(50))
print('='*50)

maioridade = homens = mulheresMenoresDeVinte = 0

while True:
    
    print('='*50)
    idade = int(input('Digite a idade da pessoa: '))
    
    if idade > 18:
        maioridade += 1
    
    sexo = ' '
    while sexo not in "MF":
        sexo = str(input('Digite o sexo da pessoa [M/F]: ')).strip().upper()
        
    if sexo == "M":
            homens += 1
            
    if sexo == "F" and idade < 20:
            mulheresMenoresDeVinte += 1
            
        
    continuar = ' '
    while continuar not in "SN":
        continuar = str(input('Deseja continuar [S/N]: ')).strip().upper()
        
    if continuar == "N":
        break
        
print(f'Na lista tem {maioridade} pessoa(s) maior de 18 anos, {homens} homem(ns) e {mulheresMenoresDeVinte} mulher(es) menores de 20 anos.')