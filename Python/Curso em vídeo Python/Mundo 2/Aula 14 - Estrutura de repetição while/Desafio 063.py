quantidadeTermos = int(input('Quantos termos da sequência de Fibonnaci deseja saber? '))

print('='*50)
print('SEQUÊNCIA DE FIBONNACI'.center(50))
print('='*50)

contador = numero = antepenultimo = penultimo = 1
print('O 1° termo da sequência de Fibonnaci é 1')

while contador != quantidadeTermos:
    print(f'O {contador + 1}° termo da sequência de Fibonacci é {numero}.')
    
    contador += 1 
    numero = penultimo + antepenultimo
    penultimo = antepenultimo
    antepenultimo = numero