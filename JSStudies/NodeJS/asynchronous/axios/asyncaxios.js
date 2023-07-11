const axios = require("axios");

const url = "https://api.github.com/users/guifreitasds"
async function start(){
    try{
        const user = await axios.get(url)
        const repos = await axios.get(user.data.repos_url)
        console.log(repos)
    
    } catch(e){
        console.log(e.message)
    }
}

start()