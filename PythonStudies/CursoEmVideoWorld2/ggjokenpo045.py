# Pedra, papel e tesoura
from random import choice
from time import sleep
elements = ['Pedra', 'Papel', 'Tesoura']
print('\033[32m-=-\033[m'*20)
print('\033[31mVamos jogar JOKENPÔ!!!\033[m')
comp = choice(elements)
user = str(input('Escolha Pedra, Papel ou Tesoura: '))
print('\033[31mJÓ')
sleep(1)
print('KEN')
sleep(2)
print('PÔ!')
sleep(1)
if user == comp:
    print(f'\033[34mEMPATAMOS, você escolheu {user} e eu {comp}!\033[m')
elif user == 'Pedra' and comp == 'Tesoura':
    print(f'\033[32mVOCÊ GANHOU DE MIM, PARABÉNS! Você escolheu {user} e eu {comp}\033[m')
elif user == 'Papel' and comp == 'Pedra':
    print(f'\033[32mVOCÊ GANHOU DE MIM, PARABÉNS! Você escolheu {user} e eu {comp}\033[m')
elif user == 'Tesoura' and comp == 'Papel':
    print(f'\033[32mVOCÊ GANHOU DE MIM, PARABÉNS! Você escolheu {user} e eu {comp}\033[m')
else:
    print(f'\033[31mHAHAHA, VOCÊ PERDEU PARA MIM! Você escolheu {user} e eu {comp}\033[m')

print('\033[32m-=-\033[m'*20)
