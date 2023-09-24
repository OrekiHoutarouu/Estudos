valores = []

for contador in range(0,5):
    valor = int(input('Digite um valor: '))
    
    if contador == 0 or valor > valores[-1]:
        valores.append(valor)
        print('Adicionado ao final da lista.')
        
    else:
        posição = 0
        while posição < len(valores):
            if valor <= valores[posição]:
                valores.insert(posição, valor)
                print(f'Adicionado na posição {posição + 1} da lista.')
                break
            
            posição += 1

print('Os valores digitados em orgem crescente foram: ', end='')
for números in valores:
    print(f'{números} ', end='')   