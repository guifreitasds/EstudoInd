# Tabuada
while True:
    n = 0
    n = int(input('Digite um número para ver sua tabuada [-1 para parar]: '))
    print('='*15)
    if n < 0:
        break
    for i in range(1, 11):
        print(f'{n:1} x {i:1} = {n*i:1}')

print('='*15)
print('Programa TABUADA encerrado!')