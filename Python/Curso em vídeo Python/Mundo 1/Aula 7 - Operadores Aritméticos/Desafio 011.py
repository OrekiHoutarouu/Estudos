a = float(input('Digite a altura da sua parede em metros: '))
l = float(input('Agora digite a largura da sua parede em metros: '))
print('A área da sua parede é de {:.2f} metros quadrados, '.format(a*l),end='')
print('e você precisará de {:.2f} litros de tinta para pintar essa parede'.format(int((a*l)/2)))