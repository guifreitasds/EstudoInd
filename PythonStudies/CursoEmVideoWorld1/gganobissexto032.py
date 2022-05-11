# Programa para checagem de ano bissexto
from datetime import date

y = int(input('Digite um ano: Digite 0 para analisar o ano atual! '))
if y == 0:
    y = date.today().year
if y % 400 == 0 or (y % 100 != 0 and y % 4 == 0):
    print(f'{y} é bissexto')
else:
    print(f'{y} não é bissexto')