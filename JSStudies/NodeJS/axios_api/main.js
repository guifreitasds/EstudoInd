const url = `http://localhost:5500/api`;

function getUser() {
    axios.get(url)
        .then(response => {
            users.innerHTML = `${JSON.stringify(response.data)}`
        })
        .catch(e => console.log(e))
}

getUser()