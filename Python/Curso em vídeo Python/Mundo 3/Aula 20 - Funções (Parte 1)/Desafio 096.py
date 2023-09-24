def área(largura, comprimento):
    área = largura * comprimento 
    print(f'A área de um terreno {largura}x{comprimento} é de {área}m²')
    
    
largura = float(input('Largura (metros): '))
comprimento = float(input('Comprimento (metros): '))
área(largura, comprimento)