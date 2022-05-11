# Programa que calcula seno, cosseno, tangente
from math import sin, cos, tan, radians

angle = float(input('Digite o ângulo desejado: '))
seno = sin(radians(angle))
cosseno = cos(radians(angle))
tangen = tan(radians(angle))

print('O seno de {:.2f} é {:.2f}'.format(angle, seno))
print('O cosseno de {:.2f} é {:.2f}'.format(angle, cosseno))
print('A tangente de {:.2f} é {:.2f}'.format(angle, tangen))
