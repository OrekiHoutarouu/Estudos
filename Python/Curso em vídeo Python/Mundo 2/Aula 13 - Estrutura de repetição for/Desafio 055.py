l = []
for c in range(1, 6):
    p = float(input(f'Digite o peso da {c}° pessoa: '))
    l.append(p)
print(f'O maior peso registrado foi de {max(l):.2f}kg e o menor foi de {min(l):.2f}kg')