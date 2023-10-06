expressao = str(input('Digite a expressão numérica: '))

pilha = []

for simbolo in expressao:
    if simbolo == '(':
        pilha.append('(')
        
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
            
        else:
            pilha.append(')')
            break
        
if len(pilha) == 0:
    print('Sua expressão numérica está correta.')
    
else:
    print('Sua expressão numérica está errada.')