from basiclibs.numeros import leiaFloat
from basiclibs.medidas import CelsiustoFah

cel = leiaFloat('Digite uma temperatura em celsius a ser convertida: ')

print(f'\033[34mA temperatura {cel}C em fahrenheit é {CelsiustoFah(cel)}F')