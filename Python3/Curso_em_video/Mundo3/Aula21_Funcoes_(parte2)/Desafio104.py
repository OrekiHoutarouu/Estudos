def leiaInt(mensagem):
    valido = False
    valor = 0
    
    while True:
        numero = str(input(mensagem))
        
        if numero.isnumeric():
            valor = int(numero)
            valido = True
        
        else:
            print('Erro, por favor digite um valor numérico inteiro válido.')
        
        if valido == True:
            break
    
    return valor


numero = leiaInt('Digite um número: ')
print(f'Você digitou o número {numero}')