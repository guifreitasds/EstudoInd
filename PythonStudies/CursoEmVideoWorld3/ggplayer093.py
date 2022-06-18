# Jogador de Futebol
matches = []
player = dict()

player['Nome'] = str(input('Digite o nome do jogador: '))
player['Partidas'] = int(input('Quantas partidas ele jogou: '))
for i in range(0, player['Partidas']):
    gols = int(input(f'Quantidade de gols na partida {i+1}: '))
    matches.append(gols)
player['Total de Gols'] = sum(matches)
print('-=-'*20)
for k, v in player.items():
    print(f'{k} tem valor {v}')

print('-=-'*20)
print(f'O jogador {player["Nome"]} fez {player["Partidas"]} partidas')
for cont, a in enumerate(matches):
    print(f'---> Na partida {cont} ele marcou {matches[cont]} gols')

print(f'Fez um total de {sum(matches)} gols')