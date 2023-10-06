aluno = []
alunos = []

while True:
    
    aluno.append(str(input('Nome: ')).strip())
    aluno.append(float(input('1° Nota: ')))
    aluno.append(float(input('2° Nota: ')))
    aluno.append((aluno[1] + aluno[2]) / 2)
    alunos.append(aluno[:])
    aluno.clear()
    
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if continuar == 'N':
        break
    
print('=' * 60)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')

for contador, informacoes in enumerate(alunos):
    print(f'{contador:<1}', end='   ')
    print(f'{informacoes[0]:<2}', end='')
    print(f'{informacoes[3]:>14.1f}')
    
notas = 0

while notas != 999:
    
    notas = int(input('Deseja ver as notas de que aluno(a)? (999 interrompe): '))
        
    if notas <= len(alunos) - 1:
        print(f'Notas do aluno(a) {alunos[notas][0]} é {alunos[notas][1]} e {alunos[notas][2]}')