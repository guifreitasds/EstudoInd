var agora = new Date()
var hora = agora.getHours()
console.log(`Agora são exatamente ${hora}:00 horas`)
if (hora >= 5 && hora < 12){
    console.log(`Bom dia!`)
} else if (hora >= 12 && hora < 18) {
    console.log(`Boa tarde!`)

} else if(hora > 0 && hora < 5) {
    console.log(`Boa madrugada!`)
}
else{
    console.log(`Boa noite!`)
}