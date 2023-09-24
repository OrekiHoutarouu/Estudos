ni = int(input('Digite um valor inteiro: '))
bc = int(input('Escolha a base de conversão, digite 1 para binário, 2 para octal e 3 para hexadecimal: '))
if bc == 1:
    print(f'{ni} em valor binário é igual a {bin(ni)[2:]}')
elif bc == 2:
    print(f'{ni} em valor octal é igual a {oct(ni)[2:]}')
elif bc == 3:
    print(f'{ni} em valor hexadecimal é igual a {hex(ni)[2:]}')    
else:
    print('Você não digitou nem 1, nem 2, nem 3, tente novamente.')