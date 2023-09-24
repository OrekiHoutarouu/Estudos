from datetime import datetime
a = datetime.today().year
n = ma = me = 0
for c in range(0,7):
    n += 1
    an = int(input(f'Digite o ano de nascimento da {n}° pessoa: '))
    if a - an > 18:
        ma += 1
    else:
        me += 1
print(f'Existem {ma} pessoa(s) maior(es) de idade, e {me} pessoa(s) menor(es) de idade na lista.')