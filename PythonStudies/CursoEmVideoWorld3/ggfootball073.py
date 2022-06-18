table = 'Corinthians', 'Palmeiras', 'São Paulo', 'Atlético-MG', 'Botafogo', 'Santos', 'Fluminense', 'Coritiba'\
,'América-MG','Avaí','Internacional', 'Athletico-PR', 'RB Bragantino', 'Flamengo', 'Goiás', 'Cuiabá', 'Atlético-GO'\
    ,'Juventude', 'Ceará', 'Fortaleza'
print(f'Lista de times do Brasileirão: {table}')
print('=-='*20)
print(f'Os 5 primeiros colocados são: {table[0:5]}')
print('=-='*20)
print(f'O Z-4 é: {table[16:20]}')
print('=-='*20)
print(f'Times em Ordem Alfábetica {sorted(table)}')
print('=-='*20)
print(f'O Flamengo na tabela é o: {table.index("Flamengo")+1}o colocado')
