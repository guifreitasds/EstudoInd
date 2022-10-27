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

def average(*n):
    media = sum(n)/len(n)
    return media
