def escreva(texto):
    tamanho = len(texto) + 4
    
    print('='*tamanho)
    print(f'{texto}'.center(tamanho))
    print('='*tamanho)


texto = str(input('Digite qualquer coisa: '))
escreva(texto)    