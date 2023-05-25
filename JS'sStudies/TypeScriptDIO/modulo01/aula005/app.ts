const array: Array<number> = [
    1,2,3,4,5
]

// console.log(array.length)
// array.push(2)
// array.pop()
// console.log(array)

// const findNum = array.find(num=>num===4)

// console.log(findNum)

const mapNum = array.forEach(num=>{
    if(num>2){
        console.log(num)
    }
})