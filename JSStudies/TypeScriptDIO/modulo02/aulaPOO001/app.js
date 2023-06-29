var User = /** @class */ (function () {
    function User(name, age) {
        this.name = name;
        this.age = age;
    }
    User.prototype.showInfo = function () {
        console.log("".concat(this.name, " tem ").concat(this.age, " anos"));
    };
    return User;
}());
var user = new User('Claudio', 20);
var secondUser = new User('Maria', 22);
user.showInfo();
secondUser.showInfo();
