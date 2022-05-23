# Sequência de Fibonacci com while

n = int(input('Digite a quantidade de termos desejada: '))
contador = 3
a1 = 0
a2 = 1
print(f'{a1} -> {a2} -> ', end='')
while contador <= n:
    a3 = a1 + a2
    print(f'{a3} -> ', end='')
    a1 = a2
    a2 = a3
    contador += 1


