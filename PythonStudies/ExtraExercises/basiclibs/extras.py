def gender(msg):
    while True:
        a = str(input(msg)).strip().upper()[0]
        if a not in 'MF':
            print('\033[31mERRO, Sexo inválido!\033[m')
        else:
            return a

