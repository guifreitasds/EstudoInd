// GRINGOTS BANK

class Account{
    name: string
    accountNumber: number
    balance: number


    constructor(fullname: string, accountNumber: number, balance: number){
        this.name=fullname
        this.accountNumber=accountNumber
        this.balance=balance
    }


    deposit(val: number){
        this.balance+=val
    }

    withdraw(val: number){
        this.balance-=val
    }
}

const acc01 = new Account('Guilherme', 1, 200)

acc01.deposit(2)
console.log(acc01)