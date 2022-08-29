/* Variaveis
-Nomes simbólicos que podem receber tipos de dados

-3 palavras para se criar uma variavel
var
let
const
*/
var clima = "Frio"
console.log (clima)

let tempo = "Ensolarado"
console.log (tempo)


const horario = 16
console.log (horario)
// a CONST não pode ser alterada por outro valor que esteja abaixo, é constante





/* Scope
-determina a visibilidade de alguma variavel do JS
*/
// no var acontece o hoisting (quando o console joga a variavel pra cima, mas sem valor)

console.log ('vai existir x antes do bloco?', x) // aqui vai existir, porém nao terá valor

{
    var x = 0
}

console.log ('vai existir x depois do bloco', x) // aqui vai existir e ter valor


//no const e no let não acontece o hoisting, isto é, não são globais, apenas locais



{
    let y = 1
    console.log ("dentro do bloco existirá valor?", y)
}


{
    const z = 2
    console.log (z)
}



