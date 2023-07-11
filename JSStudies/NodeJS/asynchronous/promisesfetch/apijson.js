const https = require('https');
const API = `https://jsonplaceholder.typicode.com/users`

https.get(API, res =>{
    console.log(res.statusCode)

})

console.log("Conectando API")

// Movimentos assíncronos ocorrem de forma que uma tarefa não precisa esperar outra terminar para ser executada
// No exemplo acima, o 2° log será mostrado primeiro que o que está dentro da chamada do método get