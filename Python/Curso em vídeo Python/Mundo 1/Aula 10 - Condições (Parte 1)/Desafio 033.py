numero1 = float(input('Digite um número: '))
numero2 = float(input('Digite outro número: '))
numero3 = float(input('Digite o terceiro número: '))

maior = numero1

if (numero3 > maior):
    maior = numero3
    
if (numero2 > maior):
    maior = numero2
    
print(f'O maior número digitado foi: {maior:.2f}.') 

menor = numero3

if (numero1 < menor):
    menor = numero1
    
if (numero2 < menor):
    menor = numero2   
     
print(f'O menor número digitado foi {menor:.2f}.')    