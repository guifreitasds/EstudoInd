words = 'Viajar', 'Elegante', 'Animal', 'Carro', 'Brasileiro', 'Abacate'

for i in words:
    print(f'\nNa palavra {i.upper()} temos: ', end='')
    for n in i:
        if n.lower() in 'aeiou':
            print(n.lower(), end=' ')