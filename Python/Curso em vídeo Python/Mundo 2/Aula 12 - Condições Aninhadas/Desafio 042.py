reta1 = float(input('Digite o valor da primeira reta: '))
reta2 = float(input('Digite o valor da segunda reta: '))
reta3 = float(input('Digite o valor da terceira reta: '))

if (reta1 < reta2 + reta3) and (reta2 < reta1 + reta3) and (reta3 < reta1 + reta2):
    print('Essas retas podem formar um triângulo.')
    
    if reta1 == reta2 == reta3:
        print('O triângulo é equilátero, pois todos os lados são iguais.')
        
    elif reta1 == reta2 != reta3 or reta1 == reta3 != reta2 or reta2 == reta3 != reta1:
        print('O triângulo é isósceles, pois somente dois lados são iguais.') 
             
    else:
        print('O triângulo é escaleno, pois todos os lados são diferentes.') 
         
          
else:
    print('Essas retas não podem formar um triângulo.')