# Programa que calcula descontos

price = float(input('Digite o preço do produto: R$')) # Pedido do preço
discount = float(input('Digite o valor do desconto(%): ')) # Pedido do desconto para o preço

print('O produto que custa R${:.2f}, com desconto de {:.2f}% vai ficar com o preço de R${:.2f}'.format
(price, discount, (price-(price*(discount/100))))) # Print do preço com desconto, com o minimo de variáveis possíveis
