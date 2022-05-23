# Progressão aritmética com while

a1 = int(input('Digite o primeiro termo da P.A: '))
r = int(input('Digite a razão da P.A: '))
contador = 0
a2 = a1

while contador < 10:
    contador = contador + 1
    print(f'{contador}º termo = {a2}')
    a2 = a2 + r