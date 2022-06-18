# Máximo e mínimo de uma lista
num = list()
mai = men = 0
for i in range(0,5):
    num.append(int(input('Digite um valor: ')))
    if i == 0:
        mai = men = num[i]
    else:
        if num[i] > mai:
            mai = num[i]
        elif num[i] < men:
            men = num[i]

print(f'A lista ficou assim: {num}')
print(f'O menor valor dos digitados foi: {men}, encontrado nas posições ', end='')
for cont, val in enumerate(num):
    if val == men:
        print(cont, end=' ')
print(f'\nO maior valor dos digitados foi: {mai}, encontrado nas posições ', end='')
for cont, val in enumerate(num):
    if val == mai:
        print(cont, end=' ')
