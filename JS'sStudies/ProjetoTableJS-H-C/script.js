

for(let a=1;a<=10;a++){
    document.querySelector( `td#team${a}`).innerHTML = localStorage.getItem(`team${a}`)
}

for(let i = 1; i<=10; i++){
    document.querySelector( `td#dado${i}t1`).innerHTML = `${Number(localStorage.getItem(`dado${i}t1`)).toFixed(1)}% ; ${Number(localStorage.getItem(`${i}x1`))}/${Number(localStorage.getItem(`${i}y1`))}`
    document.querySelector( `td#dado${i}t2`).innerHTML = `${Number(localStorage.getItem(`dado${i}t2`)).toFixed(1)}% ; ${Number(localStorage.getItem(`${i}x2`))}/${Number(localStorage.getItem(`${i}y2`))}`
    document.querySelector( `td#dado${i}t3`).innerHTML = `${Number(localStorage.getItem(`dado${i}t3`)).toFixed(1)} ; ${Number(localStorage.getItem(`${i}x3`))}/${Number(localStorage.getItem(`${i}y3`))}`
}


function alterar(id) {
    let alt = window.prompt("Qual é o novo time")
    let team = document.querySelector(`td#${id}`)
    team.innerHTML = (alt)
    localStorage.setItem(`${id}`, alt)
}

function alterarDado(id, localx, localy) {
    let dado = document.querySelector(`td#${id}`)
    let x = Number(window.prompt('Valor total: '))
    let y = Number(window.prompt('N° de Jogos: '))
    let showx = x
    let showy = y
    let media = ((x/y)*100)
    dado.innerHTML = `${media.toFixed(1)}% ; ${showx}/${showy}`
    localStorage.setItem(`${id}`, media)
    localStorage.setItem(`${localx}`, x)
    localStorage.setItem(`${localy}`, y)
}

function alterarDadoM(id, localx, localy) {
    let dado = document.querySelector(`td#${id}`)
    let x = Number(window.prompt('Valor total: '))
    let y = Number(window.prompt('N° de Jogos: '))
    let showx = x
    let showy = y
    let media = (x/y)
    dado.innerHTML = `${media.toFixed(1)} ; ${showx}/${showy}`
    localStorage.setItem(`${id}`, media)
    localStorage.setItem(`${localx}`, x)
    localStorage.setItem(`${localy}`, y)
}