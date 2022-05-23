# Leitor de pessoas
ages = []
namemai = ''
maioridadem = 0
m20 = 0

for i in range(1, 5):
    print(f'--------PESSOA {i}--------')
    name = str(input('Digite seu nome: '))
    age = int(input('Digite sua idade: '))
    ages.append(age)
    sex = str(input('Digite F ou M, de acordo com seu sexo: ')).upper().strip()
    if sex == 'M' and age > maioridadem:
        namemai = name
        maioridadem = age
    if sex == 'F' and age < 20:
        m20 += 1

print(f'A média de idade do grupo é: {sum(ages)/len(ages)}')
print(f'A maior idade entre homens é de {namemai} com {maioridadem} anos')
print(f'O número de mulheres menores que 20 anos é de {m20}')

