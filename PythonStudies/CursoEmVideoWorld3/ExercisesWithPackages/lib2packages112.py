def leiaDinheiro(phrase):
    while True:
        x = str(input(phrase)).replace(',', '.').strip()
        if x.isalpha() or x == '':
            print(f'\033[31mERRO, "{x}" não é um valor monetário!\033[m')
        else:
            break
    return float(x)
