# Classificação de atletas por idade

print('\033[31m-=-\033[m'* 20)
print('Vamos checar sua classificação de atleta pela sua idade!')

y = int(input('\033[36mDigite seu ano de nascimento: \033[m'))
currage = 2022 - y

if currage <= 9:
    print('Você está na categoria \033[36mmirim!\033[m')
elif 9 < currage <= 14:
    print('Você está na categoria \033[36minfantil!\033[m')
elif 14 < currage <= 19:
    print('Você está na categoria \033[32mJúnior!\033[m')
elif currage <= 25:
    print('Você está na categoria \033[4mSênior!\033[m')
else:
    print('Você está na categoria \033[31mMASTER!\033[m')
print('\033[31m-=-\033[m'* 20)