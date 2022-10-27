from basiclibs.numeros import *

l1 = leiaInt('Digite o primeiro lado: ')
l2 = leiaInt('Digite o segundo lado: ')
l3 = leiaInt('Digite o terceiro lado: ')

if (l1+l2) > l3 and (l2+l3) > l1 and (l3+l1) > l2:
    print('\033[34mOs lados podem formar um triângulo!\033[m')
    if l1 == l2 == l3:
        print('Triângulo Equilatero')
    elif l1 != l2 and l1 != l3:
        print('Triangulo Escaleno')
    else:
        print('Triângulo Isósceles')
else:
    print('\033[31mOs lados não podem formar um triângulo!\033[m')