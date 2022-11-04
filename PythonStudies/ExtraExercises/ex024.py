from basiclibs.numeros import leiaInt

n1 = leiaInt('Digite o preço do 1o produto: R$')
n2 = leiaInt('Digite o preço do 2o produto: R$')
n3 = leiaInt('Digite o preço do 3o produto: R$')

if n1 < n2 and n1 < n3:
    print(f'Compre o primeiro produto que custa R${n1:.2f}')
elif n2 < n1 and n2 < n3:
    print(f'Compre o segundo produto que custa R${n2:.2f}')
elif n3 < n1 and n3 < n2:
    print(f'Compre o terceiro produto que custa R${n3:.2f}')
else:
    print('Preços iguais, escolha por você!')
