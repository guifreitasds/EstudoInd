var msg = document.getElementById('msg')
var title = document.getElementById('title')
var foto = document.getElementById('foto')

var data = new Date()
var hora = data.getHours()
msg.innerHTML = `Agora são ${hora} horas`
if(hora>0 && hora<=12){
    document.body.style.backgroundColor = '#f5af8b'
    title.innerHTML = 'Bom dia!'
    foto.src = 'imgs/manha.png'
}
else if(hora>=13 && hora < 18){
    document.body.style.backgroundColor = '#925e2f'
    title.innerHTML = 'Boa tarde!'
    foto.src = 'imgs/tarde.png'
}
else {
    document.body.style.backgroundColor = '#101626'
    title.innerHTML = 'Boa noite!'
    foto.src = 'imgs/noite.png'
}