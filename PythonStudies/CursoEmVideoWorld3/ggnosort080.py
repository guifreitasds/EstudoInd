n = []

for i in range(0, 5):
    n1 = int(input('Digite o número a ser armazenado: '))
    if i == 0 or i > n[-1]:
        n.append(n1)
        print('Valor adicionado ao final da lista...')
    else:
        pos = 0
        while pos <= len(n):
            if n1 <= n[pos]:
                n.insert(pos, n1)
                print(f'Valor adicionado na posição {pos}')
                break
            pos += 1


print(n)
