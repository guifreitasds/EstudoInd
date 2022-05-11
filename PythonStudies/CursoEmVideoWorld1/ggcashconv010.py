# Conversor REAL-DÓLAR
print('\033[32m-='*20)
cash = float(input('\033[mQuanto dinheiro você tem: \033[32mR$\033[m'))

while True:
    menu = int(input('MENU: 1 - Dólar / 2 - Euro / 3 - Iene / 4 - Libra / 5 - Sair '))

    if(menu == 1):
        print('\033[31mCom R${:.2f} você pode comprar US${:.2f}\033[m'.format(cash, cash / 4.79))

    elif(menu == 2):
        print('\033[34mCom R${:.2f} você pode comprar €{:.2f}\033[m'.format(cash, cash / 5.17))

    elif(menu == 3):
        print('\033[35mCom R${:.2f} você pode comprar ¥{:.2f}\033[m'.format(cash, cash / 0.037))

    elif(menu == 4):
        print('\033[36mCom R${:.2f} você pode comprar £{:.2f}\033[m'.format(cash, cash / 6.15))

    elif(menu == 5):
        break