function verificar(){
    var atual = new Date()
    anoatual = atual.getFullYear()
    var res = document.getElementById('res')
    var fyear = document.getElementById('txtyear')
    if(fyear.value.length == 0 || fyear.value > anoatual){
        window.alert('[ERRO] Verifique os dados')
    } else {
        var fsex = document.getElementsByName('gender')
        var idade = anoatual - Number(fyear.value)
        var msg = document.getElementById('msg')
        var img = document.getElementById('img')
        if (idade > 0 && idade<=10 && fsex[1].checked){
            msg.innerHTML = `Criança de ${idade} anos`   
            img.src = 'imgs/criança-menina.png'
        } else if (idade > 0 && idade<=10 && fsex[0].checked){
            msg.innerHTML = `Criança de ${idade} anos`
            img.src = 'imgs/criança-menino.png'
        } else if(idade<=18 && fsex[1].checked){
            msg.innerHTML = `Adolescente de ${idade} anos`
            img.src = 'imgs/adolescente-menina.png'
        } else if(idade<=18 && fsex[0].checked){
            msg.innerHTML = `Adolescente de ${idade} anos`
            img.src = 'imgs/adolescente-menino.png'
        } else if(idade<=60 && fsex[1].checked){
            msg.innerHTML = `Mulher de ${idade} anos`
            img.src = 'imgs/adulto-mulher.png'
        } else if(idade<=60 && fsex[0].checked){
            msg.innerHTML = `Homem de ${idade} anos`
            img.src = 'imgs/adulto-homem.png'
        } else if(idade > 60 && fsex[1].checked){
            msg.innerHTML = `Idosa de ${idade} anos`
            img.src = 'imgs/idosa.png'
        } else{
            msg.innerHTML = `Idoso de ${idade} anos`
            img.src = 'imgs/idoso.png'
        }
    }
}