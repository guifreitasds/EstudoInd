

const { EventEmitter } = require('events');
const ev = new EventEmitter();

// Event Listener escuta o evento

ev.on('Hello World!', (message)=>{
    console.log(`Eu ouvi você, ${message}!`)
})


// Event Emitter emite o evento
ev.emit('Hello World!', "Gui")
ev.emit('Hello World!', "Gui")
ev.emit('Hello World!', "Claudio")




// Exercicio de Herança
const { inherits } = require("util")

function Person(name) {
    this.name = name;
}

inherits(Person, EventEmitter);

const claudio = new Person("Claúdio");
claudio.on('Ei', ()=>console.log("To aqui, o Claudião"))

claudio.emit('Ei')
