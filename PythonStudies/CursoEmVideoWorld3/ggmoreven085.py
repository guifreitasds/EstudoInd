n = []
imp = list()
par = list()

for i in range(0, 7):
    n1 = int(input('Digite um número: '))
    if n1 % 2 == 0:
        par.append(n1)
    else:
        imp.append(n1)
n.append(par[:])
n.append(imp[:])

print(f'Os valores pares digitados foram: {sorted(n[0])}')
print(f'Os valores ímpares digitados foram: {sorted(n[1])}')
