// Importando axios com require

const axios = require("axios");

// Puxando primeiro request com o get e retornando no 1° then outro get e logo em seguida imprimindo no 2° then os dados do 2° request!
axios.get('https://api.github.com/users/guifreitasds')
    .then(res => axios.get(res.data.repos_url))
    .then(repos => console.log(repos.data))
    .catch( err=> console.log(err))