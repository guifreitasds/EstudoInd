# Jogadores  de Futebol
matches = []
player = dict()
players = []
while True:
    player.clear()
    matches.clear()
    player['Nome'] = str(input('Digite o nome do jogador: '))
    player['Partidas'] = int(input('Quantas partidas ele jogou: '))
    for i in range(0, player['Partidas']):
        gols = int(input(f'Quantidade de gols na partida {i+1}: '))
        matches.append(gols)
    player['GolsPartida'] = matches[:]
    player['TotaldeGols'] = sum(player['GolsPartida'])
    players.append(player.copy())
    conf = str(input('Quer continuar? [S/N] ')).upper()[0]
    if conf == 'N':
        break
print('-=-'*20)
print('cod ', end='')
for m in player.keys():
    print(f'{m:<14}', end='')
print()
print('-'*60)
for k, v in enumerate(players):
    print(f'{k:>2} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*60)
while True:
    while True:
        cod = int(input('Digite o código do jogador para ver seu desempenho: '))
        if cod > len(players)-1:
            print('Erro, código do jogador não encontrado!')
        if cod <= len(players)-1:
            break
    print(f'O jogador {players[cod]["Nome"]} fez {len(players[cod]["GolsPartida"])} partidas')
    for match in range(0, len(players[cod]["GolsPartida"])):
        print(f'---> Na partida {match+1} o jogador fez {players[cod]["GolsPartida"][match]}')
    confirm = str(input('Deseja ver outro? [S/N]')).upper()[0]
    if confirm == 'N':
        break
print('<<VOLTE SEMPRE>>')
