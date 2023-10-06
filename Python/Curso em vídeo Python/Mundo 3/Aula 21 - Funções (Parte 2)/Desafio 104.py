def leiaInt(mensagem):
    válido = False
    valor = 0
    
    while True:
        número = str(input(mensagem))
        
        if número.isnumeric():
            valor = int(número)
            válido = True
        
        else:
            print('Erro, por favor digite um valor numérico inteiro válido.')
        
        if válido == True:
            break
    
    return valor


número = leiaInt('Digite um número: ')
print(f'Você digitou o número {número}')