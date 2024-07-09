contador = 1

while True:
    valorTabuada = int(input('Deseja saber a tabuada de qual valor? (Número negativo para finalizar): '))
    
    if valorTabuada < 0:
        break
    
    print('='*50)
    print('TABUADA'.center(50))
    print('='*50)
    
    for contador in range (10):
        print(f'{valorTabuada} x {contador} = {valorTabuada * contador}')
        contador += 1
        
    contador -= 10
    print('-'*28)
print('Programa finalizado, volte sempre :)')