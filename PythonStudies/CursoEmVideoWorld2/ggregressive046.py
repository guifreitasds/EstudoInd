# Contagem regressiva com For
from time import sleep
print('\033[31m-=\033[m'*20, '\n\033[34mVamos à regressiva para os fogos!!!\033[m')
for i in range(10, 0, -1):
    print(f'{i}')
    sleep(1)
print('KAAABOOMM!!!')
print('\033[31m-=-\033[m'*20)

