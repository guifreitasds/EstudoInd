# Progressão aritmética
print('\033[31m-=-\033[m'*20)
print('\033[34mVamos começar os calculos!\033[m')
n1 = int(input('Digite o primeiro termo da P.A: '))
r = int(input('Digite a razão da P.A: '))

for i in range(1, 11):
    print(f'{i}º termo: {n1}')
    n1 = n1 + r
