from basiclibs.numeros import *
from basiclibs.medidas import *

cel = leiaFloat('Digite uma temperatura em celsius a ser convertida: ')

print(f'\033[34mA temperatura {cel}C em fahrenheit é {CelsiustoFah(cel)}F')