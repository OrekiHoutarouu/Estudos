qt = int(input('Quantos termos da sequência de Fibonnaci deseja saber? '))
print(f'{"-"*5} A sequência de Fibonnaci é {"-"*5}')
con = num = ant = pen = 1
print('O 1° termo da sequência de Fibonnaci é 1')
while con != qt:
    print(f'O {con + 1}° termo da sequência de Fibonacci é {num}')
    con += 1 
    num = pen + ant
    pen = ant
    ant = num