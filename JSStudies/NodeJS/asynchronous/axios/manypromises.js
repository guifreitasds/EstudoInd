const axios = require("axios");


// Rodando 2 promises em paralelo com o metodo all
Promise.all([
    axios.get('https://api.github.com/users/guifreitasds'),
    axios.get('https://api.github.com/users/guifreitasds/repos')

])
.then(res => {
    // Na posição 0 está a API da 1a url
    console.log(res[0].data.login)
    // Na posição 1 está a API da 2a url
    console.log(res[1].data.length)
})
.catch(err => console.log(err.message))