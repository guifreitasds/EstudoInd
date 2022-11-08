from basiclibs.numeros import leiaFloat, leiaInt

tipopague='Dinheiro'

while True:
    print('1 - Filé Duplo // 2- Alcatra // 3 - Picanha')
    tipo = leiaInt('Escolha o tipo de carne que você deseja: ')
    if 1 <= tipo <= 3:
        break

qtd = leiaFloat('Escolha a quantidade em Kg: ')
card = str(input('Essa compra está sendo feita no cartão Tabajara? [S/N]'))

if tipo==1:
    if qtd>5:
        total = qtd*5.80
    else:
        total = qtd*4.90

elif tipo==2:
    if qtd>5:
        total = qtd*6.80
    else:
        total = qtd*5.90

elif tipo==3:
    if qtd>5:
        total = qtd*7.80
    else:
        total = qtd*6.90

totalbef=total
desconto=0
if card in 'SsSIMSImSiMsIM':
    desconto = (total*0.05)
    total -= desconto
    tipopague='Cartão'



print('=-=-=-=-=-=-=-=-=CUPOM FISCAL=-=-=-=-=-=-=-=-=-=')
print ("{:<12} {:<15} {:<10}".format('Tipo', 'Quantidade',  'Preço total '))
print("{:<12} {:<15} R${:<10.2f}".format(tipo, f'{qtd}Kg', totalbef))
print('----------------------------------------')
print ("{:<12} {:<15} {:<10}".format("Pagamento", "Desconto", "Valor a Pagar"))
print("{:<12} R${:<15.2f} R${:<10.2f}".format(tipopague, desconto, total))
print('=-=-=-=-=-=-==-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=')