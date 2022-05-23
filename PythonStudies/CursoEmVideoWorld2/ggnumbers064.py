# Numeros

n = int(input('Digite um número: '))
soma = 0
contador = 0
contador += 1
soma += n
menu = int(input('Digite 1 para colocar mais números, digite 999 para sair do programa: '))
while menu != 999:
    contador += 1
    soma += n
    n = int(input('Digite outro número: '))
    menu = int(input('Digite 1 para colocar mais números, digite 999 para sair do programa: '))

print(f'O total de números digitados foram {contador} e a soma entre eles é: {soma}')
