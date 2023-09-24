def ajuda(comando):
    print('='*50)
    print(f'Acessando manual do comando {comando}')
    print('='*50)
    help(comando)
    
    
comando = ''
print('='*50)
print(f'{"Sistema de ajuda PyHelp":>36}')
print('='*50)
while True:
    comando = str(input('Função ou biblioteca (fim para parar): '))
    
    if comando.upper() == 'FIM':
        break
    
    else:
        ajuda(comando)