def ficha(name='<unknown>', goals=0):
  print(f'O jogador {name} fez {goals} gol(s) no campeonato.')

nome = str(input('Jogador: '))
gols = str(input('Gols: '))
if gols.isnumeric():
  gols = int(gols)
else:
  gols = 0
if nome.strip() == '':
  ficha(goals=gols)
else:
  ficha(nome, gols)

