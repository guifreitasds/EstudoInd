# Programa que sortea um item de uma lista
from random import choice

alunos = []

add = input('Digite o nome do aluno: ')
alunos.append(add)
confirm = int(input('Digite 1 para adicionar mais um, digite 2 para parar de adicionar: '))

while confirm == 1:
    add = input('Digite o nome do aluno: ')
    alunos.append(add)
    confirm = int(input('Digite 1 para adicionar mais um, digite 2 para parar de adicionar: '))

print('O aluno sorteado foi {}'.format(choice(alunos)))