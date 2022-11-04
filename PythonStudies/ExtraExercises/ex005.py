from basiclibs.medidas import metertocenti
from basiclibs.numeros import leiaFloat

meters = leiaFloat('Digite uma medida em metros a ser convertida: ')
print(f'{meters}m em centímetros é {metertocenti(meters)}cm')
