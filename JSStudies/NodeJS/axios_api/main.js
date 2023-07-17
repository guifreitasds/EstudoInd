const url = `http://localhost:5500/api/2`;

function getUser(url) {
    axios.get(url)
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

function addUser(user) {
    axios.post(url, user)
        .then(response => console.log(response))
        .catch(e => console.log(e))
}

getUser(url)

// addUser(user)