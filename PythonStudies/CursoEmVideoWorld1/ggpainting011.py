# Pintura do parede

l = float(input('Digite a largura da parede: ')) # Pedido das medidas da parede
h = float(input('Digite a altura da parede: '))

print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(l, h, l*h)) # Print da área
print('Para pintar essa parede, você precisará de {}L de tinta'.format((l*h)/2)) # Print da quant. necess. de tinta