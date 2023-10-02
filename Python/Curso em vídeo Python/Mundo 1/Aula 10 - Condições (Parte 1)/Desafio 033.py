número1 = float(input('Digite um número: '))
número2 = float(input('Digite outro número: '))
número3 = float(input('Digite o terceiro número: '))

maior = número1

if (número3 > maior):
    maior = número3
    
if (número2 > maior):
    maior = número2
    
print(f'O maior número digitado foi: {maior:.2f}.') 

menor = número3

if (número1 < menor):
    menor = número1
    
if (número2 < menor):
    menor = número2   
     
print(f'O menor número digitado foi {menor:.2f}.')    