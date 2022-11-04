from basiclibs.numeros import leiaInt, leiaFloat

n1 = leiaInt('Digite um número inteiro: ')
n2 = leiaInt('Digite outro número inteiro: ')
n3 = leiaFloat('Digite um número real: ')

print(f'O produto do dobro do primeiro com metade do segundo é {(2*n1)*(n2/2)}')
print(f'A soma do triplo do primeiro com o terceiro é: {(3*n1)+n3}')
print(f'O terceiro elevado ao cubo é: {n3**3}')