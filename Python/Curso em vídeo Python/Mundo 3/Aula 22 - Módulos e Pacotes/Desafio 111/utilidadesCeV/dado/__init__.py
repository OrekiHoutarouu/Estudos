def leiaDinheiro(mensagem):
    válido = False
    
    while not válido:
        preçoParaValidar = str(input(mensagem)).replace(',','.').strip()
        
        if preçoParaValidar.isalpha() or preçoParaValidar == '':
            print(f'ERRO! "{preçoParaValidar}" é um preço inválido.')
            
        else:
            válido = True
            return float(preçoParaValidar)