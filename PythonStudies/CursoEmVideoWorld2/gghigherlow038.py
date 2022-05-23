# Maior e menor valor

print('\033[31m-=-\033[m'* 20)
print('\033[32mVamos descobrir qual número é o maior\033[m!')
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print(f'\033[36mO primeiro valor {n1} é maior que o segundo {n2}\033[m')
elif n2 > n1:
    print(f'\033[35mO segundo valor {n2} é maior que o primeiro {n1}\033[m')
else:
    print(f'\033[31mOs valores {n1} e {n2} são iguais!')
print('\033[31m-=-\033[m' * 20)
