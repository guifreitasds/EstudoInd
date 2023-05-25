// const num: number = 16
// if(num > 15){
//     console.log("num maior que 15")
// } else {
//     console.log("num menor que 15")
// }
var userTypes = {
    admin: 'Seja bem vindo admin',
    std: 'Seja bem vindo estudante',
    view: 'Você pode visualizar'
};
function validateUser(validation) {
    console.log(userTypes[validation]);
}
var user = 'view';
validateUser(user);
