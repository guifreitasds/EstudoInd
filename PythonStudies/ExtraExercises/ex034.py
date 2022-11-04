from basiclibs.numeros import *

notacem=0
notacinq=0
notadez=0
notacinco=0
notaum=0

print('==========CAIXA ELETRÔNICO============')
cash = leiaInt("Digite o valor a ser sacado: ")
print('======================================')

cashalt=cash

while(cash>=100):
    cash -= 100
    notacem += 1
    if(cash<100):
        break

while(cash>=50):
    cash-=50
    notacinq+=1
    if(cash<50):
        break

while(cash>=10):
    cash-=10
    notadez+=1
    if(cash<10):
        break

while(cash>=5):
    cash-=5
    notacinco+=1
    if(cash<5):
        break

while(cash>=1):
    cash-=1
    notaum+=1
    if(cash==0):
        break

print(f"""O total do saque efetuado foi de {cashalt}R$
Notas de 100: {notacem}
Notas de 50: {notacinq}
Notas de 10: {notadez}
Notas de 5: {notacinco}
Moedas de 1: {notaum} 
======================================""")

