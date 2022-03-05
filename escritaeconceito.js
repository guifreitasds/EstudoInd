/* Aqui será ensinado os tipos de dados 
e como escrevê-los, principalmente os mais usados
*/
// Tipo de dado String
console.log('Sport')
console.log("Club")
console.log(`sport ${1 + 1}`)



/* Tipo de dado Number
33 é inteiro
12.7 é floot
Nan É not a number
Infinity é infinito
*/
console.log(12 / 4)
console.log(2 / 'string here') // <--- isso vai dar NaN



/* Tipo de dado Boolean
Só existem 2 resultados - True or False
*/
console.log(true)
console.log(false)


/* Tipo de dado Null ou indefined
Null=não tem nada dentro

Undefined=é apenas indefinido, não existe
*/
console.log(null)
console.log(undefined)
console.log(null === undefined)

/* Tipo de dado Object
Existe propriedades/atributos e funcionalidades/métodos
*/ 
console.log({
    name: "Sport",
    idade: 106,
    andar: function () {
        console.log('andar')
    }

})



/* Tipo de dado Array (Vetores)
 um agrupamento de dados ou lista
 Usa-se colchetes ([])
 */
console.log([
    "Sport",
    "Club",
    "do",
    "Recife",
])

// concatenando valores de variaveis

var any, age

any = 'Sport'
age = 117

// console.log(' o ' + any + ' tem ' + age + ' anos.')


// interpolando valores de variaveis

console.log(`o ${any} tem ${age} anos`)




