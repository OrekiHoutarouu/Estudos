expressão = str(input('Digite a expressão numérica: '))

pilha = []

for símbolo in expressão:
    if símbolo == '(':
        pilha.append('(')
        
    elif símbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
        
if len(pilha) == 0:
    print('Sua expressão numérica está correta.')
    
else:
    print('Sua expressão numérica está errada.')