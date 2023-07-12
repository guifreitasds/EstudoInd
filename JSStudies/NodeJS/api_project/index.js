const exp = require("express");
const app = exp();

app.listen('3000');

let author = "Guilherme"


// app.route('/').get( (req, res)=>{
//     res.send("Hello, World!");
// } )

// middleware
app.use(exp.json())

// app.route('/').post( (req, res) => {
//     res.send(req.body)
// } )

app.route('/').get( (req, res)=>res.send(author) )

app.route('/').put( (req, res) => {
    author = req.body.author
    res.send(author)
} )