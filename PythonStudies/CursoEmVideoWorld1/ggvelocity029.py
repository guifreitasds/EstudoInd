# Radar eletrônico

velo = int(input('Qual a velocidade do carro? '))

if velo >= 81:
    print(f'Você foi multado em R${(velo-80)*7}')
else:
    print(f'Velocidade aceita! ')