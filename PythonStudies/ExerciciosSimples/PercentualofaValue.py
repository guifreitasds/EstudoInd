# Estudo IND
# Balance Percent

print('Calcule um percentual de um valor')

value1 = float(input('Insira seu valor desejado aqui: '))
percent = float(input('Insira a percentagem em valor normal (exemplo=25) aqui:'))

percentreal = percent/100

balancetotal = value1 * percentreal

p = (str(percent) +'% de ' + str(value1) + ' é igual a: ' + str(balancetotal))

print(p)