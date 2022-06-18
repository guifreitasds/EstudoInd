lista = list()

while True:
    n = int(input('Digite o valor a ser armazenado: '))
    lista.append(n)
    conf = str(input('Deseja adicionar mais valores? [S/N] ')).upper().strip()[0]
    if conf == 'N':
        break

print('=-='*20)
print(f'Os valores digitados foram: {lista}')
print(f'{len(lista)} números foram digitados')
print(f'Ordenação em forma decrescente: {sorted(lista, reverse=True)}')
if 5 in lista:
    print(f'Achei o número 5 na posição {lista.index(5)} da lista')
else:
    print('Não achei o número 5 na lista')

