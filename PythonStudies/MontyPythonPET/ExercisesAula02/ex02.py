while True:
    age = int(input('Digite sua idade: '))
    if(age<0):
        print('\033[31mERRO, digite uma idade válida\033[m')
    else:
        break

if 0<=age<=12:
    print(f'Criança de {age} anos')
elif 13<=age<=17:
    print(f'Adolescente de {age} anos')
elif age>=18:
    print(f'Adulto de {age} anos')