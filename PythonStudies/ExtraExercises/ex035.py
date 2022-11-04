from basiclibs.numeros import leiaFloat

var = leiaFloat('Digite o número a ser analisado: ')
varalt=f'{var:.2f}'

if('.00' in str(varalt)):
    print(f'{var:.0f} é um número inteiro')
else:
    print(f'{var:.2f} é um número decimal')
