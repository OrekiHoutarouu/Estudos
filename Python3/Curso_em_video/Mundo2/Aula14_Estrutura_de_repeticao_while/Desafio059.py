print(f'{"-"*5} Digite dois valores para abrir o menu de opções {"-"*5}')

opcoes = 0
while opcoes != 5:
    numero1 = float(input('Digite o primeiro valor: '))
    numero2 = float(input('Digite o segundo valor: '))
    
    opcoes = int(input(f'{"-"*5} Você deseja {"-"*5}\n[1] Somar: \n[2] Multiplicar: \n[3] Maior valor: \n[4] Digitar novos números: \n[5] Sair do programa: \nDigite o valor correspondente: '))
    
    if opcoes == 1:
        print(f'A soma entre {numero1} e {numero2} é {numero1 + numero2:.2f}.')
        
    elif opcoes == 2:
        print(f'A multiplicação entre {numero1} e {numero2} é {numero1 * numero2:.2f}.')
        
    elif opcoes == 3:
        if numero1 > numero2:
            print(f'O maior valor digitado foi {numero1:.2f}.')
            
        elif numero2 > numero1:
            print(f'O maior valor digitado foi {numero2:.2f}.')
            
        else:
            print(f'Nenhum dos valores são maiores, {numero1} e {numero2} são iguais.')
            
            
    elif opcoes > 5:
        print('O valor digitado não corresponde, tente novamente.')