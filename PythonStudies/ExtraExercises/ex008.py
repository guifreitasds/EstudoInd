from basiclibs.numeros import *

h = leiaFloat('Quanto vale a sua hora? R$')
t = leiaInt('Quantas horas você trabalha por dia? ')

print(f'\033[34mVocê ganha: R${h*(t*30)} por mês\033[m')