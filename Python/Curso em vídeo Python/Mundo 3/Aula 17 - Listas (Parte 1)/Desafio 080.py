valores = []

for contador in range(0,5):
    valor = int(input('Digite um valor: '))
    
    if contador == 0 or valor > valores[-1]:
        valores.append(valor)
        print('Adicionado ao final da lista.')
        
    else:
        posicao = 0
        
        while posicao < len(valores):
            if valor <= valores[posicao]:
                valores.insert(posicao, valor)
                
                print(f'Adicionado na posição {posicao + 1} da lista.')
                break
            
            posicao += 1

print('Os valores digitados em orgem crescente foram: ', end='')
for numero in valores:
    print(f'{numero} ', end='')   