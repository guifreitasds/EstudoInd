def leiaInt(msg):
    '''
    Semelhante ao input, lê um número inteiro, com erros tratados

    :param msg: mostra a mensagem requerida
    :return: o número inteiro
    '''
    while True:
        try:
            n = int(input(msg))
        except:
            print('\033[31mERRO, digite um número válido\033[m')
        else:
            return n

def soma(*n):
    '''
    Soma ínúmeros elementos

    :param *n: números em tupla
    :return: soma dos parâmetros(números)
    '''
    s = sum(n)
    return s

def leiaFloat(msg):
    '''
    Semelhante ao input, lê um número flutuante, com erros tratados

    :param msg: mostra a mensagem requerida
    :return: o número com ponto flutuante
    '''
    while True:
        try:
            n = float(input(msg))
        except:
            print('\033[31mERRO, digite um número válido\033[m')
        else:
            return n

def leiaFloatNota(msg):
    while True:
        try:
            n = float(input(msg))
        except:
            print('\033[31mERRO, digite um número válido\033[m')
        else:
            if n > 10:
                print('\033[31mERRO, digite uma nota de 0 a 10\033[m')
            else:
                return n

def average(*n):
    media = sum(n)/len(n)
    return media

def decimal(num=0):
    '''
    Função utilizada para diferenciar um número decimal de um número não decimal

    :param num: número requerido para análise
    :return: Nesse caso, uma string, mas em outros casos pode ser alterado para true or false
    '''
    varalt=f'{num:.2f}'
    if('.00' in str(varalt)):
        return f'{num:.0f} é um número inteiro'
    else:
        return f'{num:.2f} é um número decimal'

def simple_calculator(n1, n2, op=1):
    if op==1:
        return n1+n2
    elif op==2:
        return n1-n2
    elif op==3:
        return n1*n2
    elif op==4:
        return n1/n2
    else:
        print('\033[31mERRO, digite uma opção válida entre 1 e 4\033[m')
    