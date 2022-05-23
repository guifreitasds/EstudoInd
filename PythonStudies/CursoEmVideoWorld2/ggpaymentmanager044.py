# Gerenciador de pagamento do produto

print('\033[32m-=-'* 20)
price = float(input('Informe o valor total da compra: R$'))

modo = int(input('Escolha o modo de pagamento\033[m \n1 - À vista em dinheiro ou cheque (10% de desconto)\n2 - À vista no cartão (5% de desconto)'
      '\n3 - Em até 2x no cartão (Sem alteração)\n4 - Mais de 3x no cartão (20% de juros)'))
if modo == 1:
    total = price-(price*0.1)
    print('\033[32mO total a ser pago é de R${:.2f}\033[m'.format(total))
elif modo == 2:
    total = price-(price*0.05)
    print('\033[32mO total a ser pago é de R${:.2f}\033[m'.format(total))
elif modo == 3:
    total = price
    print('\033[32mO total a ser pago é de R${:.2f}\033[m'.format(total))
elif modo == 4:
    total = price+(price*0.2)
    print('\033[32mO total a ser pago é de R${:.2f}\033[m'.format(total))
else:
    print('\033[31mERRO\033[m')