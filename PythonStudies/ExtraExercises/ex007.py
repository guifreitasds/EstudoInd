from basiclibs.numeros import leiaFloat
from basiclibs.medidas import squareArea

lado = leiaFloat('Digite o lado do quadrado: ')

print(f'\033[34mO dobro da área {squareArea(lado)} é {2*squareArea(lado)}\033[m')