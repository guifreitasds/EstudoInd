# Adivinhe o número
import random

n = random.randint(0, 10)
print('\033[35m-=-\033[m'*20)
u = int(input('\033[36mAdivinhe o número entre 0 e 10: \033[m'))
palp = 0
palp += 1
while u != n:
    if u < n:
        print('\033[31mErrado, É MAIS, tente novamente\033[m')
    else:
        print('\033[31mErrado, É MENOS, tente novamente\033[m')
    palp += 1
    u = int(input('Adivinhe o número entre 0 e 10: '))
print(f'\033[34mPARABÉNS, o número era {n}, você acertou em {palp} tentativas!!!\033[m')
print('\033[35m-=-\033[m'*20)

