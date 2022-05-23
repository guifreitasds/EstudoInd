# Alistamento Militar

print('\033[37mSituação Militar do individuo!\033[m')

y = int(input('\033[36mDigite seu ano de nascimento: \033[m'))
milyage = 2022 - y

if milyage < 18:
    print(f'\033[31mVocê ainda não está na idade de alistamento, espere {18-milyage} ano (s)')
elif milyage == 18:
    print(f'\033[36mVocê está no período de alistamento militar, acesse o site e faça já!\033[m')
else:
    print(f'\033[31mVocê passou do prazo de alistamento em {milyage - 18} anos, acesse o site e faça já\033[m')