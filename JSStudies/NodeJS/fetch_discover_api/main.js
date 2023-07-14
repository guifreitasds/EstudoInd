const url = "http://localhost:5500/api"

function getUsers() {
    fetch(url)
    .then( (response) => response.json() )
    .then( data => document.querySelector("#renderapi").innerHTML=`${JSON.stringify(data)}` )
    .catch( e => console.error(e) )
}
getUsers()
getUser(2)
addUser()

function getUser(id) {
    fetch(`${url}/${id}`)
    .then( (response) => response.json() )
    .then( data => {
        user.innerHTML=`Seu user é: ${data.name}`
        userCity.innerHTML=`Sua cidade é: ${data.city}`
        userAvatar.src=`${data.avatar}`
    } )
    .catch( e => console.error(e) )
}


function addUser() {
    const newUser = {
        name: "guifreitasds",
        avatar: "https://avatars.githubusercontent.com/u/99972010?v=4",
        city: "Recife"
    }
    fetch(url, {
        method: "POST",
        body: JSON.stringify(newUser),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    })
        .then( (response) => response.json() )
        .then( data => {
            alertApi.textContent=`${data}`
        })
        .catch( e => console.error(e))

}
