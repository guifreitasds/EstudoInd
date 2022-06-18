# Aprimoramento de matriz

matriz = []
linha = []
soma = 0
for i in range(1, 4):
    for c in range(1, 4):
        n = (int(input(f'Digite o número da posição {i, c}: ')))
        if n % 2 == 0:
            soma += n
        linha.append(n)
    matriz.append(linha[:])
    linha.clear()
print('-=-'*20)
for a in range(0, 3):
    for fator in matriz[a]:
        print(f'[{fator}]', end='')
    print()
print('-=-'*20)
print(f'A soma de todos os valores pares é: {soma}')
print(f'A soma dos valores da terceira coluna é: {matriz[0][2]+matriz[1][2]+matriz[2][2]}')
print(f'O maior valor da segunda linha é: {max(matriz[1])}')