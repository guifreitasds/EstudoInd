import random
from time import sleep
# Jogo da Adivinhação 1.0
print('-=-' * 20)
print('Vou pensar em um número de 0 a 5, se prepare para descobrir!')
print('-=-' * 20)
n1 = random.randint(0, 5)
nuser = int(input('Adivinhe o número: '))
print('Processando...')
sleep(3)
if nuser == n1:
    print(f'Você ganhou! o numero era {n1}')
else:
    print(f'Você perdeu! o numero era {n1}')


