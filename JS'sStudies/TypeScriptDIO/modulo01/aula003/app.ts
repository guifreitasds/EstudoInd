// const num: number = 16

// if(num > 15){
//     console.log("num maior que 15")
// } else {
//     console.log("num menor que 15")
// }

const userTypes = {
    admin: 'Seja bem vindo admin',
    std: 'Seja bem vindo estudante',
    view: 'Você pode visualizar'
}

function validateUser(validation) {
    console.log(userTypes[validation as keyof typeof userTypes])
}

const user = 'view'

validateUser(user)