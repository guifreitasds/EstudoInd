def area():
    print('Controle de Terrenos')
    print('-'*25)
    l = float(input('LARGURA (m): '))
    c = float(input('COMPRIMENTO (m): '))
    a = l*c
    print(f'A área de um terreno {l:.1f}x{c:.1f} é de {a:.1f}m2')


# Main
area()