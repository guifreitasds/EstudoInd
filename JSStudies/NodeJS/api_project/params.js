const exp = require("express");
const app = exp();

app.listen('3000');

app.use(exp.json())

app.route('/').post( (req, res) => {
    const {nome, cidade, times_favoritos} = req.body
    res.send(`Meu nome é ${nome}, moro em ${cidade} e meus times favoritos são ${times_favoritos}`)
} )