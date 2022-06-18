from random import randint
from time import sleep
n = []
tot = []
print('-=-'*20)
print('VAMOS JOGAR NA LOTERIA!')
print('-=-'*20)
u = int(input('Digite o número de jogos desejados: '))

for a in range(0, u+1):
    if a == 0:
        print()
    else:
        tot.append(n[:])
        n.clear()
    for i in range(0, 6):
        numb = (randint(1, 60))
        if numb not in n:
            n.append(numb)
        else:
            pass
print(f'SORTEANDO {u} JOGOS')
for cont, j in enumerate(tot):
    print(f'Jogo {cont+1}: {j}')
    sleep(1)
print('=-='*20)