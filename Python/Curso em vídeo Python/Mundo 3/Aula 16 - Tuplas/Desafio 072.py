extenso = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'

número = int(input('Digite um número entre 0 e 20: '))
while número < 0 or número > 20:
    número = int(input('Valor inválido, digite um número entre 0 e 20: '))
    
print(f'O número {número} em extenso é {extenso[número]}')