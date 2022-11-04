from basiclibs.numeros import leiaFloat
from basiclibs.medidas import circleArea

raio = leiaFloat('Digite o raio do círculo: ')
print(f'\033[34mA área do círculo com raio {raio} é de {circleArea(raio)}\033[m')