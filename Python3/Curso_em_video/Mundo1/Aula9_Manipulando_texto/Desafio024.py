cidade = str(input('Digite o nome da sua cidade: ')).lower().strip()

cidadeSeparada = cidade.split()

print(f'O nome da sua cidade começa com Santo? {"santo" in cidadeSeparada[0]}.')