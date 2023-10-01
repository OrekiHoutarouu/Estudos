import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
    
except:
    print('O site pudim.com.br não está acessível no momento')
else:
    print('O site pudim.com.br está acessível no momento')