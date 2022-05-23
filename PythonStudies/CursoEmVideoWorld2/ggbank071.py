# Simulador de Caixa Eletrônico

print('='*20)
print('{:^20}'.format('PYTHON BANK'))
print('='*20)
cedcin = cedvin = cedd = cedum = 0

withdraw = int(input('Digite o valor a ser sacado: R$'))
total = withdraw
while total >= 50:
    cedcin += 1
    total -= 50
while total >= 20:
    cedvin += 1
    total -= 20
while total >= 10:
    cedd += 1
    total -= 10
while total >= 1:
    cedum += 1
    total -= 1
    if total == 0:
        break
if cedcin > 0:
    print(f'Total de {cedcin} cédulas de R$50')
if cedvin > 0:
    print(f'Total de {cedvin} cédulas de R$20')
if cedd > 0:
    print(f'Total de {cedd} cédulas de R$10')
if cedum > 0:
    print(f'Total de {cedum} cédulas de R$1')

''' FORMA DO CURSO (+ OTIMIZADO QUE O MEU CÓDIGO)
print('='*20)
print('{:^20}'.format('PYTHON BANK'))
print('='*20)
withdraw = int(input('Digite o valor a ser sacado: R$'))
total = withdraw
ced = 50
totced = 0
while True:
    if total>=ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        if ced == 20:
            ced = 10:
        if ced == 10:
            ced = 1
        if total == 0:
            break
'''