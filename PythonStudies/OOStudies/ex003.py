class Account:
    def set_details(self, name, balance=0):
        self.name=name
        self.balance=balance

    def display(self):
        print(f'Hi, {self.name}, your balance is US${self.balance}')

    def withdraw(self, value):
        self.balance-=value

    def deposit(self, value):
        self.balance+=value

while True:
    print(f'{"-="*4}GRINGOTS BANK{"-="*4}')
    print(f"1-Create account")
    esc = int(input('Choose: '))
    if (esc == 1):
        x = input('Type your name: ')
        y = float(input('What is your balance? US$'))
        p1 = Account()
        p1.set_details(x, y)
        break

while True:
    print(f'{"-="*4}GRINGOTS BANK{"-="*4}')
    print(f"""1-Update account
2-Check balance
3-Withdraw
4-Deposit
5-Logout
{"-="*16}""")
    esc = int(input('Choose: '))
    if(esc==1):
        x=input('Type your name: ')
        y=float(input('What is your balance?'))
        p1=Account()
        p1.set_details(x,y)
    elif (esc == 2):
        p1.display()
    elif(esc==3):
        withvalue=float(input('How much you want to withdraw: US$'))
        p1.withdraw(withvalue)
        print(f'{"-="*4}US${withvalue} WITHDRAW SUCEED{"-="*4}')
    elif (esc == 4):
        depvalue = float(input('How much you want to deposit: US$'))
        p1.deposit(depvalue)
        print(f'{"-="*4}US${depvalue} DEPOSIT SUCEED{"-="*4}')
    elif(esc==5):
        print(f'{"-="*4}SEE YOU SOON{"-="*4}')
        break