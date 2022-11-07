from basiclibs.numeros import leiaFloat

straw = leiaFloat('Digite a quantidade de morangos em Kg: ')
apples = leiaFloat('Digite a quantidade de maçãs em Kg: ')

if straw>5:
    strawvalue=2.20
else:
    strawvalue=2.50

if apples>5:
    applesvalue=1.80
else:
    applesvalue=1.50

total = (straw*strawvalue) + (apples*applesvalue)

if total>25 or straw+apples==8:
    total -= (total*0.10)

print(f'O preço total da sua compra é de R${total}')
