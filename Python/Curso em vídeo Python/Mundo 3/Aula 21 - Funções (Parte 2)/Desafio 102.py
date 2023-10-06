def fatorial(numero, show = 0):
    """
    Calcula o fatorial de algum número
    :parâmetro número: Número que vai ser calculado o fatorial
    :parâmetro show: Mostra ou não a conta
    :retorno: Retorno do valor do fatorial
    """
    contador = numero
    fatorial = 1
    
    if show == True:
        while contador != 0:
            print(f'{contador}', end=' ')
            
            if contador != 1:
                print('x', end=' ')
                
            fatorial *= contador
            contador -= 1
            
        return fatorial
        
    else:
        while contador != 0:
            fatorial *= contador
            contador -= 1
            
        return fatorial
    
    
help(fatorial)
print(fatorial(5, show=True))