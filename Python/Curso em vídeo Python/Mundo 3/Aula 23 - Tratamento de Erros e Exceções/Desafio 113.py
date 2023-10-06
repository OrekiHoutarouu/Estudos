def leiaInt(mensagem):
    while True:
        try:
            numeroInteiro = int(input(mensagem))
                   
        except:
            print('ERRO! Digite um valor inteiro válido.')
        
        else:
            return numeroInteiro


def leiaFloat(mensagem):
    while True:
        try:
            numeroReal = float(input(mensagem))
 
        except:
            print('ERRO! Digite um valor Real válido.')
        
        else:
            return numeroReal


numeroInteiro = leiaInt('Digite um número inteiro: ')
numeroReal = leiaFloat('Digite um número Real: ')

print(f'O valor inteiro digitado foi {numeroInteiro} e o real foi {numeroReal}.')