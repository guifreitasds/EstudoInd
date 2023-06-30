// setInterval estabelece uma função para rodar de X em X milissegundos

const timeOut = 1000;
const checker = ()=> console.log(`CHECKING...`);

let timer = setInterval(checker, timeOut);
setTimeout(()=> clearInterval(timer), 3020)
