from lib.Arquivo import *
from lib.Interface import *
from time import sleep

arquivo = 'pessoas.txt'

if arquivoExiste(arquivo) == False:
    criarArquivo(arquivo)
    
while True:
    resposta = menu(['Ver pessoa(s) cadastrada(s)', 'Cadastrar nova pessoa', 'Sair do programa'])
    
    if resposta > 3 or resposta < 1:
        print('ERRO! Digite uma opção válida')
    
    elif resposta == 1:
        cabecalho('PESSOAS CADASTRADAS')
        lerArquivo(arquivo)
        
    elif resposta == 2:
        cabecalho(f'NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arquivo, nome, idade)
        
    elif resposta == 3:
        cabecalho('Saindo do programa...')
        break
    
    sleep(2)