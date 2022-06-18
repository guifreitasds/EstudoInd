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