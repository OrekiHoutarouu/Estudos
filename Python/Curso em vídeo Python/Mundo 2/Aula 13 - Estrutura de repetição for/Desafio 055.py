lista = []

for contador in range(1, 6):
    peso = float(input(f'Digite o peso da {contador}° pessoa: '))
    lista.append(peso)
    
print(f'O maior peso registrado foi de {max(lista):.2f}kg e o menor foi de {min(lista):.2f}kg.')