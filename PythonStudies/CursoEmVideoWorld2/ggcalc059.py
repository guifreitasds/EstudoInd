# Calculadora com while

n1 = int(input('Digite o numero 1: '))
n2 = int(input('Digite o numero 2: '))
u = 0

while u != 5:
    u = int(input('''Digite a opção desejada
    1 - Somar
    2 - Multiplicar
    3 - Maior número
    4 - Digitar novos números 
    5 - Sair'''))
    if u == 1:
        soma = n1 + n2
        print(f'\033[34mA soma entre {n1} e {n2} é igual a: {soma}\033[m')
    elif u == 2:
        mul = n1 * n2
        print(f'\033[34mA multiplicação entre {n1} e {n2} é igual a: {mul}\033[m')
    elif u == 3:
        if n1 > n2:
            print(f'\033[34mO maior número entre {n1} e {n2} é {n1}\033[m')
        elif n2 > n1:
            print(f'\033[34mO maior número entre {n1} e {n2} é {n2}\033[m')
        else:
            print(f'\033[34mOs valores {n1} e {n2} são iguais\033[m')
    elif u == 4:
        n1 = int(input('Digite o novo numero 1: '))
        n2 = int(input('Digite o novo numero 2: '))
    else:
        print('\033[31mOpção inválida, tente novamente\033[m')


