# Tabuada com laço for
n = int(input('\033[34mDigite o número para ver sua tabuada: '))
for i in range(1, 11):
    print(f'{n} x {i:2} = {n*i}')
