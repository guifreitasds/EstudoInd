const exp = require("express");
const app = exp()

app.listen('3000')


app.route('/').get( (req, res)=>{
    res.send("Hello, World!")
} )