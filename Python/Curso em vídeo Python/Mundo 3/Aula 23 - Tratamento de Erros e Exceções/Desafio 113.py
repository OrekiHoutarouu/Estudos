def leiaInt(mensagem):
    while True:
        try:
            númeroInteiro = int(input(mensagem))
                   
        except:
            print('ERRO! Digite um valor inteiro válido.')
        
        else:
            return númeroInteiro


def leiaFloat(mensagem):
    while True:
        try:
            númeroReal = float(input(mensagem))
 
        except:
            print('ERRO! Digite um valor Real válido.')
        
        else:
            return númeroReal


númeroInteiro = leiaInt('Digite um número inteiro: ')
númeroReal = leiaFloat('Digite um número Real: ')

print(f'O valor inteiro digitado foi {númeroInteiro} e o real foi {númeroReal}.')