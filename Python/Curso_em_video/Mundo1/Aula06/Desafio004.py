mensagem = input('Digite algo: ')

print('O tipo primitivo é',type(mensagem))
print('Só tem letra?',mensagem.isalpha())
print('Só tem número?',mensagem.isnumeric())
print('Tem letra e número?',mensagem.isalnum())
print('Tá em letra minúscula?',mensagem.islower())
print('Tá em letra maiúscula?',mensagem.isupper())
print('Tem espaço?',mensagem.isspace())