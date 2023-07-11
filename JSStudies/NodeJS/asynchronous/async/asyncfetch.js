const url = `https://api.github.com/users/guifreitasds`
async function start(){
    try{
        // Uso de constantes para as duas buscas com o metodo fetch API para buscar todos meus repositórios
        const user = await fetch(url).then((r)=>r.json())
        const repos = await fetch(user.repos_url).then( rep => rep.json())
        console.log(repos)
    
    } catch (e){
        console.log(e)
    } finally{
        console.log("Nada")
    }
}

// Chamada da função assíncrona
start()