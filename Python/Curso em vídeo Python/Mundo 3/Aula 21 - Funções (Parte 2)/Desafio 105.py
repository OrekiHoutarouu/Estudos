def notas(*notas, situação = False):
    """
    Analisador de notas e situações de alunos.
    :parâmetro notas: Uma ou mais notas de alunos
    :parâmetro situação: Situação do aluno, opcional
    :retorno: Dicionário com informações dos alunos
    """
    informações = {}
    informações['Total'] = len(notas)
    informações['Maior'] = max(notas)
    informações['Menor'] = min(notas)
    informações['Média'] = sum(notas) / len(notas)
    
    if situação == True:
        if informações['Média'] < 5:
            informações['Situação'] = 'Ruim'
        
        elif informações['Média'] >= 5 and informações['Média'] < 7:
            informações['Situação'] = 'Razoável'
            
        else:
            informações['Situação'] = 'Boa'
            
    return informações
   
    
resposta = notas(9, 10, 5.5, 2.5, 8.5, situação=True)
print(resposta)