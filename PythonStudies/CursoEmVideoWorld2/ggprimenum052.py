# Descubra se um número é primo ou não

n = int(input('\033[36mDigite um número: \033[m'))
fator = 0

for i in range(1, 11):
    if (n%i == 0):
        fator = fator + 1

if fator == 2:
    print('\033[32mÉ primo\033[m')
else:
    print('\033[31mNão é primo\033[m')