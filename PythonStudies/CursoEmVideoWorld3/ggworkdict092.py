person = dict()

person['name'] = str(input('Digite seu nome: '))
birthy = int(input('Digite seu ano de nascimento: '))
person['idade'] = 2022 - birthy
person['carteira'] = int(input('Digite o número da sua carteira de trabalho: (0 não tem) '))

if person['carteira'] != 0:
    person['contratação'] = int(input('Digite o ano em que foi contratado: '))
    person['salario'] = float(input('Digite seu salário: R$'))
    person['aposentadoria'] = (person['contratação'] - birthy) + 35

for k, v in person.items():
    print(f'{k} tem valor {v}')