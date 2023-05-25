interface Animal {
    nome: string,
    peso: number,
    som?: string
}

const animal_1: Animal = {
    nome: 'cachorro',
    peso: 2
}

const outroAnimal: Animal = {
    nome: 'gato',
    peso: 5,
    som: 'miau'
}

const arrayAnimal: Animal[] = [
    animal_1,
    outroAnimal
]

console.log(arrayAnimal)

