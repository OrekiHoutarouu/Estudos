def area(largura, comprimento):
    area = largura * comprimento 
    print(f'A área de um terreno {largura}x{comprimento} é de {area}m²')
    
    
largura = float(input('Largura (metros): '))
comprimento = float(input('Comprimento (metros): '))
area(largura, comprimento)