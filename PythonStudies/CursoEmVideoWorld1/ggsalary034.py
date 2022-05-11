# Algoritmo aumento salarial

s = float(input('Digite o seu salário: '))

if s > 1250:
    aumento = s + (s * 0.1)
    print(aumento)
else:
    aumentomax = s + (s * 0.15)
    print(aumentomax)