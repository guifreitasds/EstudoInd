# Armazenador de números
numbers = list()

while True:
    add = (int(input('Digite o valor desejado: ')))
    if add not in numbers:
        numbers.append(add)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor não inserido, já existente')
    conf = str(input('Deseja adicionar mais valores? [S/N]')).upper().strip()[0]
    if conf == 'N':
        break
print('=-='*20)
print(f'Os valores digitados ordenando-os são: {sorted(numbers)}')
