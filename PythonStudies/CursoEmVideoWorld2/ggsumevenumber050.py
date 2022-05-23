# Soma de números pares
sum = 0
for i in range(1, 7):
    n = int(input(f'Digite o {i}º número: '))
    if n%2==0:
        sum += n
print(f'\033[34mA soma total dos números é: {sum}\033[m')
print('\033[31m-=-\033[m'*20)
