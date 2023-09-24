n = 1
s = 0
r = 'S'
l = []
while r != 'N':
    n = float(input('Vá digitando números para saber a média entre eles e qual o maior e o menor valor: '))
    r = str(input('Deseja digitar novos números? [S/N]: ')).upper().strip()
    s += n
    l.append(n)
print(f'A média entre os números digitados é {s/len(l):.2f}')
print(f'O maior número digitado foi {max(l):.2f} e o menor número digitado foi {min(l):.2f}')