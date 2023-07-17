const url = `http://localhost:5500/api/`;

function getUser(id) {
    axios.get(`${url}${id}`)
        .then(response => {
            users.innerHTML = `${JSON.stringify(response.data)}`
            userAvatar.src = `${response.data.avatar}`
        })
        .catch(e => console.log(e))
}

const user = {
    name: "Guilherme Freitas",
    avatar: "https://avatars.githubusercontent.com/u/99972010?v=4",
    city: "Recife"
}

const updatedUser = {
    name: "Lucas",
    avatar: "https://avatars.githubusercontent.com/u/99782517?v=4",
    city: "Recife"
}

function addUser(user) {
    axios.post(url, user)
        .then(response => console.log(response))
        .catch(e => console.log(e))
}

function updateUser(id, user) {
    axios.put(`${url}${id}`, user)
        .then(response => console.log(response))
        .catch(e => console.log(e))
}

getUser(2)

updateUser(2, updatedUser)

// addUser(user)