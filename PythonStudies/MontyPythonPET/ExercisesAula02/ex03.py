time = float(input('Digite o tempo da sua viagem em horas: '))
averagev = float(input('Digite a velocidade média da sua viagem em Km/h: '))

distance = time*averagev

used_l = distance/12

print('\n==========VIAGEM COMPLETA==========')
print(f'Você obteve uma velocidade média de {averagev}Km/h\nGastou {time} horas\nPercorreu uma distância de {distance}Km\nE acabou gastando {used_l}L de Combustível\n===================================')