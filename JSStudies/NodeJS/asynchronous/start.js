const axios = require("axios");

axios.get('https://api.github.com/users/guifreitasds')
    .then(res => axios.get(res.data.repos_url))
    .then(repos => console.log(repos.data))
    .catch( err=> console.log(err))