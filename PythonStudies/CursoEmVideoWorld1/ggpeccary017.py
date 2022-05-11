# Programa que calcula a hipotenusa

co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))

hypo = (co ** 2 + ca ** 2) ** (1/2)

print('A hipotenusa vai medir {:.2f}'.format(hypo))
