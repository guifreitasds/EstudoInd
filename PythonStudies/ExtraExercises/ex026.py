from basiclibs.numeros import leiaFloat

sal = leiaFloat('Digite seu salário: R$')
percent = 0

if sal <= 280:
    liquid = (sal*0.2)+sal
    percent = 20
elif 280 < sal <= 700:
    liquid = (sal*0.15)+sal
    percent = 15
elif 700 < sal <= 1500:
    liquid = (sal*0.1)+sal
    percent = 10
elif sal > 1500:
    liquid = (sal*0.05)+sal
    percent = 5

print(f'Salário antes do reajuste: R${sal}')
print(f'Porcentagem de aumento de {percent}%')
print(f'O valor aumentado foi de: R${liquid-sal}')
print(f'O novo salário com aumento é de: R${liquid}')