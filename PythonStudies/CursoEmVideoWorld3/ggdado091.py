from random import randint
from time import sleep
from operator import itemgetter
players = dict()
players['p1'] = randint(1, 6)
players['p2'] = randint(1, 6)
players['p3'] = randint(1, 6)
players['p4'] = randint(1, 6)
ranking = []
print('Valores Sorteados:')
for k, v in players.items():
    print(f'O jogador {k} tirou {v}')
    sleep(1)
ranking = sorted(players.items(), key=itemgetter(1), reverse=True)
print('     -=-Ranking dos jogadores-=-')
for a, b in enumerate(ranking):
    print(f'      {a+1} Lugar = {b[0]} que tirou {b[1]}')
    sleep(1)



