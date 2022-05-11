    # Programa resolutor de triângulos
print('\033[0;34m-=-' * 20)

r1 = float(input('\033[1;34mDigite o valor da 1a reta: '))
r2 = float(input('\033[1;34mDigite o valor da 2a reta: '))
r3 = float(input('\033[1;34mDigite o valor da 3a reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
        print('\033[4;32mOs segmentos podem formar um triângulo')
else:
        print('\033[4;31mOs segmentos não podem formar um triângulo')