from basiclibs.numeros import *

exce = leiaFloat('Digite a quantidade de quilos de peixe pescados: ')

price = (exce-50)*4

print(f'Para {exce}Kg de peixe, a multa será de R${price:.2f}')