nome = str(input(('Digite seu nome: '))).strip()
espaços = nome.count(' ')

print(f'Seu nome com todas as letras maiúsculas é {nome.upper()}')
print(f'Seu nome com todas as letras minúsculas é {nome.lower()}')
print(f'Seu nome tem {len(nome) - espaços} letras ao todo.')

nomes = nome.split()
print(f'Seu primeiro nome tem {len(nomes[0])} letras.')