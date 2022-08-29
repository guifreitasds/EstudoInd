var inittxt = document.getElementById('init')
var endtxt = document.getElementById('end')
var passtxt = document.getElementById('pass')

function contar(){
    var res = document.getElementById('res')
    var init = Number(inittxt.value)
    var end = Number(endtxt.value)
    var pass = Number(passtxt.value)
    if (init == 0 || end == 0){
        // Verificador de dados
        res.innerHTML = 'Impossível efetuar a contagem!'
    } else{
        res.innerHTML = `Contando: <br>`
        if (pass == 0){
            // Tratamento, caso a razão do usuário for nula
            window.alert('Impossível efetuar com passo 0, utilizaremos passo 1')
            pass = 1
        }
        if(init < end){
            // Contagem crescente
            for(i = init; i<=end; i+=pass){
                res.innerText += `${i} \u{1F449}`
        }
        } else{
            // Contagem decrescente
            for(i = init; i>=end; i-=pass){
                res.innerText += `${i} \u{1F449}`
        }
        }
    res.innerHTML += `\u{1F3C1}`
    }
}