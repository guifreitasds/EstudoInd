const express = require('express');
const app = express()

app.set("view engine", "ejs");

app.get("/", (req, res) => {

    const items = [
        {
            title: "D",
            message: "esenvolver é legal!"
        },
        {
            title: "E",
            message: " codar também é!"
        },
        {
            title: "V",
            message: "eja você mesmo e comece a codar hoje!"
        }
    ]

    const subtitle = "EJS é uma linguagem de modelagem para criação de páginas HTML em JS"
    res.render("pages/index", {
        qualitys: items,
        subtitle: subtitle
    })
})

app.get("/about", (req, res) => {
    res.render("pages/about")
})

app.listen(8080);
console.log("entrou!!!")