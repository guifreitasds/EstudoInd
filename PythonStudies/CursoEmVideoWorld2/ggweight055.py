# Leitor de pesos
pesos = []
for i in range(1, 6):
    kg = float(input('Digite seu peso em Kg: '))
    pesos.append(kg)

print(f'O maior peso é {max(pesos)}Kg')
print(f'O menor peso é {min(pesos)}Kg')

