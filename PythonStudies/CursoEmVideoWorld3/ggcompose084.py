pessoas = list()
dados = list()
pes = []
lev = []
tot = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    pessoas.append(dados[:])
    tot += 1
    if dados[1] <= 70:
        lev.append(dados[:])
    elif dados[1] >= 100:
        pes.append(dados[:])
    dados.clear()
    conf = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if conf == 'N':
        break
print(pessoas)
print(f'{tot} Pessoas foram cadastradas')
print(f'As pessoas mais leves são: ',end='')
for p in lev:
    print(f'{p[0]} com {p[1]}Kg ')
print(f'\nAs pessoas mais pesadas são: ')
for c in pes:
    print(f'{c[0]} com {c[1]}Kg')