from basiclibs.numeros import *

dd = leiaInt('Digite o dia: ')
mm = leiaInt('Digite o mês: ')
yy = leiaInt('Digite o ano: ')

if dd > 31 or dd < 0 or 12<mm<0:
    print('\033[31mData inválida\033[m')
else:
    print('\033[34mData válida\033[m')

