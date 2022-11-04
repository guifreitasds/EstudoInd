from basiclibs.numeros import leiaInt, soma

n1 = leiaInt('Digite um número: ')
n2 = leiaInt('Digite outro número: ')

print(f'\033[34mA soma de {n1}+{n2} é igual a {soma(n1, n2)}')