from basiclibs.numeros import leiaFloat, leiaInt

control = 0

while True: 
    control=0
    name = str(input('Nome de usuário: '))
    if(len(name)>3):
        control+=1
    age = leiaInt('Idade: ')
    if(0<=age<=150):
        control+=1
    salary = leiaFloat('Salário: R$')
    if salary>0:
        control+=1
    sex = str(input('Sexo: [M/F] '))
    if sex in 'MmFf':
        control+=1
    civest = str(input('Estado Civil [S - Solteiro, C - Casado, V - Viuvo, D - Divorciado]'))
    if civest in 'SsCcVvDd':
        control+=1
    if control==5:
        break