# Algoritmo Conversor de temperaturas

C = float(input('Qual a temperatura em °C: ')) # Pedido da temperatura ao usuário

menu = int(input('1 - Fahrenheit / 2 - Kelvin ')) # Pedido da escolha de conversão

# Conversões
while True:
    if menu == 1:
        print(f'A temperatura de {C}°C corresponde a {(C * 1.8)+32}°F')
    if menu == 2:
        print("A temperatura de {}°C corresponde a {}K".format(C, C + 273))
    else:
        break
