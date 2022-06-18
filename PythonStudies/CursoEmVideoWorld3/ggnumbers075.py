numbers = int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: '))\
    ,int(input('Digite um número: '))
print(f'A lista de números digitados foi: {numbers}')
print('-=-'*20)
print(f'O valor 9 apareceu {numbers.count(9)} vezes')
if 3 in numbers:
    print(f'O valor 3 aparaceu primeiro na {numbers.index(3)+1} posição')
else:
    print('O valor 3 não aparece na tupla!')
print(f'Os números pares foram: ', end='')
for i in numbers:
    if i % 2 == 0:
        print(i, end=' ')
