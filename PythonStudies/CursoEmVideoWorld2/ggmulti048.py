# Números impares multiplos de 3, entre 1 e 500
n = []
print('\033[31m-=-\033[m'*20)
for i in range(1, 500):
    if i%2==1 and i%3==0:
        n.append(i)
print(f'A soma total é: {sum(n)}')
print('\033[31m-=-\033[m'*20)
