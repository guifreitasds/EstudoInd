let num = [3,2,1,5,6,7,9,10,0]
// 1a forma
// for(i=0; i<num.length; i++){
//     console.log(`A posição ${i} tem valor ${num[i]}`)
// }

for(let pos in num){
    console.log(`A posição ${pos} tem valor ${num[pos]}`)
}
console.log(`${num.indexOf(11)}`)
