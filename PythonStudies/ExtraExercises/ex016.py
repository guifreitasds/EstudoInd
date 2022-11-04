from basiclibs.medidas import area
from basiclibs.numeros import leiaFloat

print('\033[34mVamos Pintar uma parede!\033[m')
b = leiaFloat('Digite a largura em metros: ')
h = leiaFloat('Digite a altura em metros: ')

tarea = area(b, h)
litros = tarea/3
price = litros/18
latas = price/80

print(f'Para pintar uma parede de {tarea}m2, você precisa de {latas:.2f} latas de tinta de 18L que custará R${price:.2f}')