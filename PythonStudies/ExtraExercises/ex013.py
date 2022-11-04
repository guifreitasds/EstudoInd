from basiclibs.numeros import leiaFloat

height = leiaFloat('Digite sua altura em metros: ')
sex = str(input('Digite seu sexo: '))[0]

if sex in 'Mm':
    ideal = (72.7*height) - 58
if sex in 'Ff':
    ideal = (62.1 * height) - 44.7

print(f'Seu peso ideal é {ideal:.2f}Kg')