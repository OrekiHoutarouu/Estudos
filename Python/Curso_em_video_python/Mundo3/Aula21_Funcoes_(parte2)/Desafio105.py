def notas(*notas, situacao = False):
    """
    Analisador de notas e situações de alunos.
    :parâmetro notas: Uma ou mais notas de alunos
    :parâmetro situação o: Situação do aluno, opcional
    :retorno: Dicionário com informações dos alunos
    """
    informacoes = {}
    informacoes['Total'] = len(notas)
    informacoes['Maior'] = max(notas)
    informacoes['Menor'] = min(notas)
    informacoes['Média'] = sum(notas) / len(notas)
    
    if situacao == True:
        if informacoes['Média'] < 5:
            informacoes['Situação'] = 'Ruim'
        
        elif informacoes['Média'] >= 5 and informacoes['Média'] < 7:
            informacoes['Situação'] = 'Razoável'
            
        else:
            informacoes['Situação'] = 'Boa'
            
    return informacoes
   
    
resposta = notas(9, 10, 5.5, 2.5, 8.5, situacao=True)
print(resposta)