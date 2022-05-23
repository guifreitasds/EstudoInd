# Aprovando Empréstimo para compra de casa
print('\033[31m-=-\033[m'*20)
print('\033[4mAprovando Empréstimo para compra de casa\033[m')

hp = float(input('\033[32mQual é o preço da casa? R$\033[m'))
salary = float(input('\033[32mQual o salario do comprador? R$\033[m'))
y = int(input('\033[35mEm quantos anos será pago?\033[m '))

prestation = hp/(y*12)
print('O valor da parcela mensal será de R${:.2f}'.format(prestation))

if prestation <= (0.3 * salary):
    print('\033[32mEmpréstimo aprovado! Boa estadia.\033[m')
elif prestation > (0.3 * salary):
    print('\033[31mEmpréstimo Negado, seu salário não é suficiente!\033[m')


print('\033[31m-=-'*20)