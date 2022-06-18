import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('O pudim não está acessível')
else:
    print('O pudim está acessivel')
