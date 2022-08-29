var numtxt = document.getElementById('num')
var seltab = document.getElementById('tabuada')

function tabuada() {
    if(numtxt.value.length == 0){
        window.alert('Por favor, digite um número!')
    } else{
        var num = Number(numtxt.value)
        seltab.innerHTML = ''
        for(i = 1; i<=10; i++){
            let doc = document.createElement('option')
            doc.value = `tab${i}`
            doc.text += `${num} x ${i} = ${num*i}`
            seltab.appendChild(doc)
        }
    }
}
