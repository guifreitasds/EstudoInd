from basiclibs.numeros import leiaFloat, average

n1 = leiaFloat('Digita a 1a nota: ')
n2 = leiaFloat('Digita a 2a nota: ')
n3 = leiaFloat('Digita a 3a nota: ')
n4 = leiaFloat('Digita a 4a nota: ')

print(f'\033[34mA média das 4 notas foi {average(n1, n2, n3, n4):.2f}\033[m')