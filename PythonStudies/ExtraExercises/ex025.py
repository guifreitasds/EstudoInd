from basiclibs.numeros import leiaInt

n1 = leiaInt('Digite um número: ')
n2 = leiaInt('Digite outro número: ')
n3 = leiaInt('Digite o último número: ')

if n1 > n2 and n1 > n3:
    print(f'{n1},', end='')
    if n2 > n3:
        print(f' {n2}, {n3}', end='')
    else:
        print(f' {n3}, {n2}', end='')
elif n2 > n1 and n2 > n3:
    print(f'{n2},', end='')
    if n1 > n3:
        print(f' {n1}, {n3}', end='')
    else:
        print(f' {n3}, {n1}', end='')
elif n3 > n1 and n3 > n2:
    print(f'{n3},', end='')
    if n1 > n2:
        print(f' {n1}, {n2}', end='')
    else:
        print(f' {n2}, {n1}', end='')
else:
    print('Números iguais')