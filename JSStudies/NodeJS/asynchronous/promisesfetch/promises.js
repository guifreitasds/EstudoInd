// Promessas são alguma coisa que espera ser cumprida
// Podem ser pending, ou seja, aguardando serem executadas
// Podem ser fulfilled, ou seja concluídas com sucesso
// Podem ser rejecteds, ou seja, rejeitadas
// Podem ser settleds, ou seja, mesmo com sucesso ou erro ela foi concluída

console.log("Pedir comida")
let aceitar = true

const promise = new Promise((resolve, reject)=>{
    if(aceitar){
        return resolve("Pedido aceito")
    }
    return reject("Pedido Negado")
})
console.log("Aguardando")


promise
    .then(result => console.log(result))
    .catch(erro => console.log(erro))
    .finally(()=>console.log("Finalizado!!!"))