def leiaInt(mensagem):
    while True:
        try:
            numeroInteiro = int(input(mensagem))
                   
        except:
            print('ERRO! Digite um valor inteiro válido.')
        
        else:
            return numeroInteiro


def linha(tamanho = 42):
    return '=' * tamanho


def cabecalho(texto):
    print(linha())
    print(texto.center(42))
    print(linha())
    
    
def menu(lista):
    cabecalho('MENU PRINCIPAL')
    
    for contador, item in enumerate(lista):
        print(f'{contador + 1} - {item}')
        
    print(linha())
    
    opcao = leiaInt('Sua Opção: ')
    return opcao