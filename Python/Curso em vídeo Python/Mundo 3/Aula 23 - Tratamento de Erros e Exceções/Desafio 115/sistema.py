from lib.arquivo import *
from lib.interface import *
from time import sleep

arquivo = 'pessoas.txt'

if arquivoExiste(arquivo):
    print('Arquivo encontrado com sucesso!')

else:
    print('Arquivo não encontrado.')
    
while True:
    resposta = menu(['Ver pessoa(s) cadastrada(s)', 'Cadastrar nova pessoa', 'Sair do programa'])
    
    if resposta > 3 or resposta < 1:
        print('ERRO! Digite uma opção válida')
    
    elif resposta == 1:
        cabeçalho(f'Opção {resposta}')
        
    elif resposta == 2:
        cabeçalho(f'Opção {resposta}')
        
    elif resposta == 3:
        cabeçalho('Saindo do programa...')
        break
    
    sleep(2)