var numbers = []
var resultado = document.querySelector('div#phrases')

function isNumber(n) {
    if(n>=0 && n<=100){
        return true
    } else{
        return false
    }
}


function isPresent(n, l) {
    if(l.indexOf(Number(n)) == -1){
        return true
    }else{
        return false
    }
}


function add() {
    let numbertxt = document.getElementById('n')
    let res = document.getElementById('numbers')
    let number = Number(numbertxt.value)
    resultado.innerHTML = ''

    if (isNumber(number) && isPresent(number, numbers)){
        numbers.push(number)
        let doc = document.createElement('option')
        doc.value = `tab${number}`
        doc.text += `Valor ${number} adicionado`
        res.appendChild(doc)
    } else{
        window.alert('Valor inválido ou já existente!')
    }
    numbertxt.value = ''
    numbertxt.focus()
}
function finish() {
    if(numbers.length==0){
        window.alert('Por favor, adicione valores na lista!')
    }else{
        sum = 0
        resultado.innerHTML += `<p>Ao todo são ${numbers.length} números cadastrados</p>`
        resultado.innerHTML += `<p>O maior valor foi ${Math.max.apply(null, numbers)}</p>`
        resultado.innerHTML += `<p>O maior valor foi ${Math.min.apply(null, numbers)}</p>`
        for(i in numbers){
            sum += numbers[i]
        }
        resultado.innerHTML += `<p>A soma de todos os valores é ${sum}</p>`
        resultado.innerHTML += `<p>A média entre os valores é de ${sum/numbers.length}</p>`
    }
}