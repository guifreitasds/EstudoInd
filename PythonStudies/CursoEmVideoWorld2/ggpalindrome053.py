# Descubra se uma frase é palindromo

phr = str(input('Digite uma palavra ou frase: ')).strip().replace(' ', '').upper()
fator = -1
p = 0
for i in range(len(phr)-1, -1, -1):
    fator = fator + 1
    if phr[i] == phr[fator]:
        pass
    else:
        p = p + 1


if p == 0:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')
