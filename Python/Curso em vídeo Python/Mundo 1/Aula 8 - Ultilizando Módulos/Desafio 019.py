from random import choice

aluno1 = str(input('Digite o nome do aluno 1: ')).strip()
aluno2 = str(input('Digite o nome do aluno 2: ')).strip()
aluno3 = str(input('Digite o nome do aluno 3: ')).strip()
aluno4 = str(input('Digite o nome do aluno 4: ')).strip()

alunos = [aluno1, aluno2, aluno3, aluno4]

print(f'O aluno escolhido foi {choice(alunos)}.')