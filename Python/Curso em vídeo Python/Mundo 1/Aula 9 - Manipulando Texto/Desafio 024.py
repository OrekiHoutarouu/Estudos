c = str(input('Digite o nome da sua cidade: ')).lower().strip()
cs = c.split()
print('O nome da sua cidade começa com Santo? {}'.format('santo' in cs[0]))