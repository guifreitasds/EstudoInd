class User {
    name: string
    age: number

    constructor(name: string, age: number){
        this.name=name
        this.age=age
    }

    showInfo(){
        console.log(`${this.name} tem ${this.age} anos`)
    }
}

const user = new User('Claudio', 20)
const secondUser = new User('Maria', 22)


user.showInfo()
secondUser.showInfo()
