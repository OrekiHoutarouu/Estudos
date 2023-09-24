print(f'{"-"*5} Digite dois valores para abrir o menu de opções {"-"*5}')
m = 0
while m != 5:
    n1 = float(input('Digite o primeiro valor: '))
    n2 = float(input('Digite o segundo valor: '))
    m = int(input(f'{"-"*5} Você deseja {"-"*5}\n[1] Somar: \n[2] Multiplicar: \n[3] Maior valor: \n[4] Digitar novos números: \n[5] Sair do programa: \nDigite o valor correspondente: '))
    if m == 1:
        print(f'A soma entre {n1} e {n2} é {n1+n2:.2f}.')
    elif m == 2:
        print(f'A multiplicação entre {n1} e {n2} é {n1*n2:.2f}.')
    elif m == 3:
        if n1 > n2:
            print(f'O maior valor digitado foi {n1:.2f}')
        elif n2 > n1:
            print(f'O maior valor digitado foi {n2:.2f}')
        else:
            print(f'Nenhum dos valores são maiores, {n1} e {n2} são iguais.')
    elif m > 5:
        print('O valor digitado não corresponde, tente novamente.')