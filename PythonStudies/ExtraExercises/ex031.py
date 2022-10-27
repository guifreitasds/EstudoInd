from basiclibs.numeros import *

while True:
    n1 = leiaInt("Digite o número (Menor que 1000) a ser lido: ")
    if(n1<1000):
        break
    print("Número inválido")

stringn1 = str(n1)
strres = ""
if len(stringn1)==3:
    for key, i in enumerate(stringn1):
        plural = ''
        if int(i)>1:
            plural = 's'
        if key == 0:
            strres += f'{i} Centena{plural}, '
        if key == 1:
            strres += f'{i} Dezena{plural} e '
        if key == 2:
            strres += f'{i} Unidade{plural}'

if len(stringn1)==2:
    for key, i in enumerate(stringn1):
        plural = ''
        if int(i)>1:
            plural = 's'
        if key == 0:
            strres += f'{i} Dezena{plural} e '
        if key == 1:
            strres += f'{i} Unidade{plural}'

if len(stringn1)==1:
    for key, i in enumerate(stringn1):
        plural = ''
        if int(i)>1:
            plural = 's'
        if key == 0:
            strres += f'{i} Unidade{plural}'
print(strres)