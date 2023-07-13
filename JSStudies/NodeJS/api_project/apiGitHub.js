const exp = require("express");
const axi = require("axios");
const app = exp();

app.listen("3000");


app.route("/").get( (req, res) => {
    axi.get('https://api.github.com/users/guifreitasds')
    .then( (result) => {
        res.send(`<img src="${result.data.avatar_url}"></img>`)
    } )
    .catch( e => console.log(e))
} )