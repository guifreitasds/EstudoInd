from basiclibs.numeros import leiaFloat
n1 = leiaFloat('Digite o 1o número: ')
n2 = leiaFloat('Digite o 2o número: ')

if n1 > n2:
    print(f'{n1} é o maior')
elif n2 > n1:
    print(f'{n2} é o maior')
else:
    print(f'{n1} e {n2} são iguais!')