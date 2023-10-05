numeros = 1
somaDeNumeros = 0
novosNumeros = 'S'
listaDeNumeros = []

while novosNumeros != 'N':
    numeros = float(input('Vá digitando números para saber a média entre eles e qual o maior e o menor valor: '))
    novosNumeros = str(input('Deseja digitar novos números? [S/N]: ')).upper().strip()
    somaDeNumeros += numeros
    listaDeNumeros.append(numeros)
    
print(f'A média entre os números digitados é {somaDeNumeros/len(listaDeNumeros):.2f}.')
print(f'O maior número digitado foi {max(listaDeNumeros):.2f} e o menor número digitado foi {min(listaDeNumeros):.2f}.')