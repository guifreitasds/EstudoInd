# Resolutor de maior idade
fator = 0
for i in range(1, 8):
    y = int(input('Digite seu ano de nascimento: '))
    if 2022 - y >= 21:
        fator += 1
print(f'A quantidade de maiores de idade é: {fator}')
print(f'A quantidade de menores de idade é: {7-fator}')