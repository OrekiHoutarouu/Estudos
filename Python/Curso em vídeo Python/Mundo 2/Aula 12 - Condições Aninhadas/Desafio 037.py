númeroInteiro = int(input('Digite um valor inteiro: '))
baseDeConversão = int(input('Escolha a base de conversão, digite 1 para binário, 2 para octal e 3 para hexadecimal: '))

if baseDeConversão == 1:
    print(f'{númeroInteiro} em valor binário é igual a {bin(númeroInteiro)[2:]}.')
    
elif baseDeConversão == 2:
    print(f'{númeroInteiro} em valor octal é igual a {oct(númeroInteiro)[2:]}.')
    
elif baseDeConversão == 3:
    print(f'{númeroInteiro} em valor hexadecimal é igual a {hex(númeroInteiro)[2:]}.') 
       
else:
    print('Digite uma opção válida.')