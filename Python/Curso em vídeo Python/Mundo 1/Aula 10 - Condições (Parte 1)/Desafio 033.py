n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite o terceiro número: '))
ma = n1
if (n3 > ma):
    ma = n3
if (n2 > ma):
    ma = n2
print(f'O maior número digitado foi: {ma}') 
me = n3
if (n1 < me):
    me = n1
if (n2 < me):
    me = n2    
print(f'O menor número digitado foi {me}')    