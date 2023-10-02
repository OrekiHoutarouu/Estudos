preço = float(input('Digite o preço do produto: R$'))

print(f'Esse produto com desconto de 5% fica por R${preço - (preço * (5 / 100)):.2f}.')