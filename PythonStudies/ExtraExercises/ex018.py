from basiclibs.numeros import leiaInt

n1 = leiaInt('Digite um número: ')

if n1 > 0:
    print('Positivo!')
elif n1 < 0:
    print('Negativo!')
else:
    print('Nulo!')