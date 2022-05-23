# Progressão aritmética com while

a1 = int(input('Digite o primeiro termo da P.A: '))
r = int(input('Digite a razão da P.A: '))
contador = 0
a2 = a1
plus = 1
total = 8
while plus != 0:
    total += plus
    while contador <= total:
        contador += 1
        print(f'{contador}º termo = {a2}')
        a2 += r
    plus = int(input('Quantos termos você deseja ver a mais? '))

print(f'P.A terminada com {contador} termos')