def leiaDinheiro(mensagem):
    valido = False
    
    while not valido:
        precoParaValidar = str(input(mensagem)).replace(',','.').strip()
        
        if precoParaValidar.isalpha() or precoParaValidar == '':
            print(f'ERRO! "{precoParaValidar}" é um preço inválido.')
            
        else:
            valido = True
            return float(precoParaValidar)