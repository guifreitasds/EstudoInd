# Criação de Matriz

matriz = []
linha = []

for i in range(1, 4):
    for c in range(1, 4):
        n = (int(input(f'Digite o número da posição {i, c}: ')))
        linha.append(n)
    matriz.append(linha[:])
    linha.clear()
for a in range(0, 3):
    for fator in matriz[a]:
        print(f'[{fator}]', end='')
    print()