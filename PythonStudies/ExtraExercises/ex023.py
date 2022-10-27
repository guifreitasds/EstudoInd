from basiclibs.numeros import *

n1 = leiaInt('Digite um número: ')
n2 = leiaInt('Digite outro número: ')
n3 = leiaInt('Digite o último número: ')

if n1 > n2 and n1 > n3:
    print(f'O maior número é {n1}')
    if n2 > n3:
        print(f'E o menor é {n3}')
    else:
        print(f'E o menor é {n2}')
elif n2 > n1 and n2 > n3:
    print(f'O maior número é {n2}')
    if n1 > n3:
        print(f'E o menor é {n3}')
    else:
        print(f'E o menor é {n1}')
elif n3 > n1 and n3 > n2:
    print(f'O maior número é {n3}')
    if n1 > n2:
        print(f'E o menor é {n2}')
    else:
        print(f'E o menor é {n1}')
else:
    print('Números iguais')