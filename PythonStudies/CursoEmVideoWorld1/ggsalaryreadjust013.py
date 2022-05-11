# Programa de aumento salarial

s = float(input('Digite o salário a ser aumentado: R$'))
a = float(input('Digite o aumento em %: '))

print('Um funcionário que ganhava R${:.2f}, passará a receber, com {:.2f}%, R${:.2f}'.format(s, a, s+(s*(a/100))))
