// Maneira de escrever promessas em funções

let aceitar=true;
const promise = new Promise((resolve, reject)=>{
    if(aceitar){
        return resolve("Pedido aceito")
    }
    return reject("Pedido Negado")
})

async function start(){
    try{
        const result = await promise
        console.log(result)
    } catch(e){
        console.log(e)
    } finally{
        console.log("Pedido finalizado")
    }
    
}

start()