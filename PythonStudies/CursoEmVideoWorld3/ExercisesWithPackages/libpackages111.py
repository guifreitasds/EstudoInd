
def resumo(price, raiser, lower):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(price)}')
    print(f'Dobro do preço: \t{dobro(price, True)}')
    print(f'Metade do preço: \t{metade(price, True)}')
    print(f'{raiser}% de aumento: \t{aumentar(price, raiser, True)}')
    print(f'{lower}% de redução: \t{diminuir(price, lower, True)}')
    print('-'*30)

def metade(num=0, form=False):
    res = num / 2
    if form == True:
        return moeda(res)
    else:
        return res

def dobro(num=0, form=False):
    res = num * 2
    if form == True:
        return moeda(res)
    else:
        return res

def aumentar(num=0, percent=0, form=False):
    res = (num+(num*(percent/100)))
    if form == True:
        return moeda(res)
    else:
        return res

def diminuir(num=0, percent=0, form=False):
    res = (num-(num*(percent/100)))
    if form == True:
        return moeda(res)
    else:
        return res

def moeda(num = 0, moeda = 'R$'):
    return f'{moeda}{num:.2f}'.replace('.', ',')