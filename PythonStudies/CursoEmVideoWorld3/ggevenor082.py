lista = list()
par = []
impar = []

while True:
    n = int(input('Digite o valor a ser armazenado: '))
    lista.append(n)
    conf = str(input('Deseja adicionar mais valores? [S/N] ')).upper().strip()[0]
    if conf == 'N':
        break

pos = 0
while pos <= len(lista)-1:
    if lista[pos] % 2 == 0:
        par.append(lista[pos])
    else:
        impar.append(lista[pos])
    pos += 1
print(f'A lista completa é: {lista}')
print(f'Os números pares digitados foram: {par}')
print(f'Os números ímpares digitados foram: {impar}')







''' OUTRA FORMA DE FAZER 
while True:
    n = int(input('Digite o valor a ser armazenado: '))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    conf = str(input('Deseja adicionar mais valores? [S/N] ')).upper().strip()[0]
    if conf == 'N':
        break

print(f'A lista completa é: {lista}')
print(f'Os números pares digitados foram: {par}')
print(f'Os números ímpares digitados foram: {impar}')'''

