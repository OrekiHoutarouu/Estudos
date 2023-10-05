numero = int(input('Digite um número para saber seu fatorial: '))
contador = numero
fatorial = 1

while contador > 0:
    print(f'{contador}', end='')
    
    if contador != 1:
        print(' x ', end='')
        
    fatorial *= contador
    contador -= 1
    
print(f' = {fatorial}')