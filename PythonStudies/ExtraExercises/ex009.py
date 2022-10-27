from basiclibs.numeros import *
from basiclibs.medidas import *

fahr = leiaFloat('Digite uma temperatura em fahrenheit a ser convertida: ')

print(f'\033[34mA temperatura {fahr}F em celsius é {FahtoCelsius(fahr)}C\033[m')