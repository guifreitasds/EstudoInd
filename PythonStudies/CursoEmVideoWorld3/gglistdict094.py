# Cadastro de Pessoas
person = dict()
people = list()
sum = 0

while True:
    person['Nome'] = str(input('Nome: ')).strip()
    while True:
        person['Sexo'] = str(input('Sexo: [M/F]')).strip().upper()[0]
        if person['Sexo'] in 'MF':
            break
    person['Idade'] = int(input('Idade: '))
    sum += person['Idade']
    people.append(person.copy())
    person.clear()
    while True:
        conf = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        if conf in 'SN':
            break
        print('ERRO, responda apenas com S ou N')
    if conf == 'N':
        break
average = sum / len(people)
print('-=-'*30)
print(f'A) No total temos {len(people)} pessoas cadastradas!')
print(f'B) A média de idade é de {average:.2f} anos')
print('C) As mulheres cadastradas foram ', end='')
for v in people:
    if v['Sexo'] == 'F':
        print(f'{v["Nome"]} ',end='')
print()
print('D) Lista das pessoas que estão acima da média de Idade')
for a in people:
    if a['Idade'] >= average:
        print(a)
print('<<ENCERRADO>>')



