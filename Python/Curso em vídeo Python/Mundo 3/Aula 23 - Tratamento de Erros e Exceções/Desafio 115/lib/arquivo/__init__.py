def arquivoExiste(nome):
    try:
        arquivo = open(nome, 'rt')
        arquivo.close()
        
    except FileNotFoundError:
        return False
    
    else:
        return True
    

def criarArquivo(nome):
    try:
        arquivo = open(nome, 'wt+')
        arquivo.close
        
    except:
        print('Houve um erro na criação do arquivo.')
    
    else:
        print(f'Arquivo {nome} criado com sucesso!')
        
    
def lerArquivo(nome):
    from lib.interface import cabeçalho
    
    try:
        arquivo = open(nome, 'rt', encoding = 'utf-8')
    
    except:
        print('Houve um erro ao ler o arquivo.')
        
    else:
        for linha in arquivo:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<34} {dado[1]} anos')
        
        
def cadastrar(arquivo, nome = 'Desconhecido', idade = 0):
    try:
        arquivo = open(arquivo, 'at')

    except:
        print('Houve um erro na abertura do arquivo.')
        
    else:
        try:
            arquivo.write(f'{nome};{idade}\n')
        
        except:
            print('Houve um erro ao cadastrar os dados.')
        
        else:
            print(f'Novo registro de {nome} adicionado!')