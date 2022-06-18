# Descoberta do maior valor
from time import sleep
def maior(* values):
    print('-'*30)
    print('Analisando os valores...')
    for i in values:
        print(f'{i} ', end='')
        sleep(0.5)
    print(f'foram informados {len(values)} valores ao todo')
    print(f'O maior valor entre eles é: {max(values)}')


maior(5, 4, 0)
maior(1, 10, 200)