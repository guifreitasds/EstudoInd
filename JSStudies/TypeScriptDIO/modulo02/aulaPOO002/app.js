// GRINGOTS BANK
var Account = /** @class */ (function () {
    function Account(fullname, accountNumber, balance) {
        this.name = fullname;
        this.accountNumber = accountNumber;
        this.balance = balance;
    }
    Account.prototype.deposit = function (val) {
        this.balance += val;
    };
    Account.prototype.withdraw = function (val) {
        this.balance -= val;
    };
    return Account;
}());
var acc01 = new Account('Guilherme', 1, 200);
acc01.deposit(2);
console.log(acc01);
