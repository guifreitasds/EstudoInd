from basiclibs.numeros import leiaInt

tipo = ''
while True:
    tipo = str(input('Escolha o tipo de combustível: [A - Alcool, G - Gasolina]'))
    if(tipo=='A' or tipo=='G'):
        break

litros = leiaInt('Quantos litros você deseja? ')

if tipo=='G':
    total = litros*2.50
    if litros<=20:
        desconto = (2.50*0.04)*litros
        total -= desconto
        print(f'O total da compra foi de: R${total:.2f}')
    else:
        desconto = (2.50*0.06)*litros
        total -= desconto
        print(f'O total da compra foi de: R${total:.2f}')

elif tipo=='A':
    total = litros*1.90
    if litros<=20:
        desconto = (1.90*0.03)*litros
        total -= desconto
        print(f'O total da compra foi de: R${total:.2f}')
    else:
        desconto = (1.90*0.05)*litros
        total -= desconto
        print(f'O total da compra foi de: R${total:.2f}')
