# Algoritmo de aluguel de carros

d = int(input('Quantos dias de uso? ')) # Pedidos aos usuários
km = float(input('Quantos km rodados? '))

# Total a pagar
print('O total a pagar é R${:.2f}'.format((d*60)+(km*0.15)))
