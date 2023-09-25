def leiaInt(mensagem):
    ok = False
    valor = 0
    
    while True:
        número = str(input(mensagem))
        
        if número.isnumeric():
            valor = int(número)
            ok = True
        
        else:
            print('Erro, por favor digite um valor numérico inteiro válido.')
        
        if ok == True:
            break
    
    return valor


número = leiaInt('Digite um número: ')
print(f'Você digitou o número {número}')