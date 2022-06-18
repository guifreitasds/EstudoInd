# Funções
from random import randint
from time import sleep
numb = []


def sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(0, 5):
        n = randint(0, 10)
        numb.append(n)
        print(f'{n} ', end='')
        sleep(0.7)
    print('Pronto!', end='')

def somapar():
    soma = 0
    for s in numb:
        if s%2 == 0:
            soma += s
    print(f'\nA soma dos números pares de {numb} é: {soma}')


sorteia()
somapar()