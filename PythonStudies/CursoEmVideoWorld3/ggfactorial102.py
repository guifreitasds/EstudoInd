def fatorial(num, show=False):
    """
    --> Calcula o fatorial de um número
    :param num: número a ser calculado
    :param show: (opcional) mostra a operação completa do fatorial
    :return:
    """
    factor = num
    for i in range(num-1, 0, -1):
        factor *= i
    print(f'O fatorial de {num} é igual a {factor}')
    if show == True:
        for a in range(num, -1, -1):
            if a > 1:
                print(f'{a} x ', end='')
            elif a == 0:
                print(f'1 = {factor}')

us = int(input('Qual número para ver o fatorial: '))
conf = str(input('Gostaria de ver as operações? ')).upper().strip()[0]
if conf == 'S':
    fatorial(us, show=True)
else:
    fatorial(us)