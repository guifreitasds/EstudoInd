# mais numeros

n = int(input('Digite um número: '))
soma = 0
maior = 0
menor = 0
contador = 0
contador += 1
soma += n
if n > maior:
    maior = n
    menor = n
menu = int(input('Digite 1 para colocar mais números, digite 2 para sair do programa: '))
while menu != 2:
    contador += 1
    soma += n
    n = int(input('Digite outro número: '))
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
    menu = int(input('Digite 1 para colocar mais números, digite 2 para sair do programa: '))

print(f'A média dos números digitados é: {soma/contador:.2f}')
print(f'O maior valor é {maior}')
print(f'O menor valor é {menor}')