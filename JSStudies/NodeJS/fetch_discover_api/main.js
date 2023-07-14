const url = "http://localhost:5500/api"

function getUsers() {
    fetch(url)
    .then( (response) => response.json() )
    .then( data => document.querySelector("#renderapi").innerHTML=`${JSON.stringify(data)}` )
    .catch( e => console.error(e) )
}

getUser(1)

function getUser(id) {
    fetch(`${url}/${id}`)
    .then( (response) => response.json() )
    .then( data => {
        document.querySelector('#user').innerHTML=`Seu user é: ${data.name}`
        document.querySelector("#userCity").innerHTML=`Sua cidade é: ${data.city}`
        userAvatar.src=`${data.avatar}`
    } )
    .catch( e => console.error(e) )
}


