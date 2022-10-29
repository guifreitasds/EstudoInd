from basiclibs.numeros import *

def gender(msg):
    while True:
        a = str(input(msg)).strip().upper()[0]
        if a not in 'MF':
            print('\033[31mERRO, Sexo inválido!\033[m')
        else:
            return a

def verificarMedia(*n):
    media = average(*n)
    if media==10:
        print(f'\033[32mAluno aprovado com distinção, média {media:.2f}\033[m')
    elif media>=7:
        print(f'\033[34mAluno aprovado com média {media:.2f}\033[m')
    else:
        print(f'\033[31mAluno reprovado com média {media:.2f}\033[m')