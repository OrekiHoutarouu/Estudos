numeroInteiro = int(input('Digite um valor inteiro: '))
baseDeConversao = int(input('Escolha a base de conversão, digite 1 para binário, 2 para octal e 3 para hexadecimal: '))

if baseDeConversao == 1:
    print(f'{numeroInteiro} em valor binário é igual a {bin(numeroInteiro)[2:]}.')
    
elif baseDeConversao == 2:
    print(f'{numeroInteiro} em valor octal é igual a {oct(numeroInteiro)[2:]}.')
    
elif baseDeConversao == 3:
    print(f'{numeroInteiro} em valor hexadecimal é igual a {hex(numeroInteiro)[2:]}.') 
       
else:
    print('Digite uma opção válida.')