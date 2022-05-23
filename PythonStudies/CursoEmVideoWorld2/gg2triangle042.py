# Analisador de Triângulos

# Programa resolutor de triângulos
print('\033[0;34m-=-\033[m' * 20)

r1 = float(input('\033[1;34mDigite o valor da reta 1: '))
r2 = float(input('Digite o valor da reta 2: '))
r3 = float(input('Digite o valor da reta 3: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[4;32mOs segmentos podem formar um triângulo\033[m')
    if r1 == r2 and r2 == r3:
        print('\033[36mOs segmentos formam um triângulo equilátero')
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print('Os triângulos formam um triângulo isósceles')
    else:
        print('Os triângulos formam um triângulo escaleno')

else:
    print('\033[4;31mOs segmentos não podem formar um triângulo')
print('\033[0;34m-=-\033[m' * 20)