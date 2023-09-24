f = str(input('Digite uma frase: ')).strip().lower()
print('Na sua frase a letra "a" aparece {} vezes'.format(f.count('a')))
print('A letra "a" aparece pela primeira vez na posição {}'.format(f.find('a') + 1))
print('A letra "a" aparece pela última vez na posição {}'.format(f.rfind('a') + 1))