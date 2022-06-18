from ggcoin109 import moeda
def resumo(price, raiser, lower):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda.moeda(price)}')
    print(f'Dobro do preço: \t{moeda.dobro(price, True)}')
    print(f'Metade do preço: \t{moeda.metade(price, True)}')
    print(f'{raiser}% de aumento: \t{moeda.aumentar(price, raiser, True)}')
    print(f'{lower}% de redução: \t{moeda.diminuir(price, lower, True)}')
    print('-'*30)