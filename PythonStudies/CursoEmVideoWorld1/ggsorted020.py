# Programa que sortea a ordem de uma lista
from random import shuffle

alunos = []

add = input('Digite o nome do aluno: ')
alunos.append(add)
confirm = int(input('Digite 1 para adicionar mais um, digite 2 para parar de adicionar: '))

while confirm == 1:
    add = input('Digite o nome do aluno: ')
    alunos.append(add)
    confirm = int(input('Digite 1 para adicionar mais um, digite 2 para parar de adicionar: '))

shuffle(alunos)
print('A ordem sorteada foi: ')
print(alunos)
