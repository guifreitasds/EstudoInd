from basiclibs.extras import gender

x = gender('Digite seu sexo: ')

if x == 'F':
    print(f'{x} - Feminino')
else:
    print(f'{x} - Masculino')