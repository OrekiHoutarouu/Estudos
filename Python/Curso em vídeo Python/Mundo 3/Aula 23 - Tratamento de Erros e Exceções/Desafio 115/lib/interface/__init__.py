def leiaInt(mensagem):
    while True:
        try:
            númeroInteiro = int(input(mensagem))
                   
        except:
            print('ERRO! Digite um valor inteiro válido.')
        
        else:
            return númeroInteiro


def linha(tamanho = 42):
    return '=' * tamanho


def cabeçalho(texto):
    print(linha())
    print(texto.center(42))
    print(linha())
    
    
def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    
    for contador, item in enumerate(lista):
        print(f'{contador + 1} - {item}')
        
    print(linha())
    
    opção = leiaInt('Sua Opção: ')
    return opção