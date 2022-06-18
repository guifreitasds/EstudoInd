def vote(y):
    age = 2022 - y
    if age < 16:
        return 'NEGADO'
    elif 18 > age >= 16 or age >= 65:
        return 'OPCIONAL'
    else:
        return 'OBRIGATÓRIO'


# Programa Main
year = int(input('Digite seu ano de nascimento: '))
print(f'Com a idade de {2022-year}, seu direito de voto nas eleições é {vote(year)}')
