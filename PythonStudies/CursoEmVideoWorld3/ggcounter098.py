from time import sleep
def contador(ini, fim, pas):
    if pas > 0 and ini > fim:
        pas *= -1
    if pas < 0 and fim > ini:
        pas *= -1
    elif pas == 0:
        pas = 1
    for i in range(ini, fim, pas):
        print(i, end=' ')
        sleep(0.5)
    print('FIM!')

contador(1, 11, 1)
print()
contador(10, -1, -2)
print()
st = int(input('Digite o inicio da sequência: '))
end = int(input('Digite o final da sequência: '))
r = int(input('De quanto em quanto eu devo contar? '))
contador(st, end, r)
