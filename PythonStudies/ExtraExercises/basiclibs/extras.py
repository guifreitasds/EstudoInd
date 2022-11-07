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

def amongus():
    control=0
    print('=-=-=-=-=-=INTERROGATÓRIO-=-=-=-=-=-=')
    p1 = str(input('Você telefonou para a vítima?'))
    if p1 in 'SsSimsimSIMsImSiM':
        control+=1
    p2 = str(input('Você esteve no local do crime?'))
    if p2 in 'SsSimsimSIMsImSiM':
        control+=1
    p3 = str(input('Você mora perto da vítima?'))
    if p3 in 'SsSimsimSIMsImSiM':
        control+=1
    p4 = str(input('Você devia para a vítima?'))
    if p4 in 'SsSimsimSIMsImSiM':
        control+=1
    p5 = str(input('Você já trabalhou com a vítima?'))
    if p5 in 'SsSimsimSIMsImSiM':
        control+=1

    if control==2:
        return 'Suspeito'
    elif control==3 or control==4:
        return 'Cumplice'
    elif control==5:
        return '\033[31mASSASSINO\033[m'
    else:
        return '\033[34mInocente\033[m'