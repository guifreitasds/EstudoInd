function getCommits(repo) {
    fetch(`https://api.github.com/repos/guifreitasds/${repo}/commits`)
      .then(async (res) => {
        if(!res.ok){
            throw new Error(res.status);
        }

        var data = await res.json();

        for (let i = 0; i < 7; i++) {
            const item = data[i];

            const sha = item.sha;
            let divintocommits = document.createElement('div')
            let divcommits = document.querySelector('div.commits');
            
            divintocommits.innerHTML = `
            <a class="commit-one shadow-box" href="https://github.com/guifreitasds/EstudoInd/commit/${sha}">
                <strong>${item.commit.message}</strong>
                <span>${item.commit.author.date}</span>
            </a>
            `
            
            divcommits.appendChild(divintocommits);
        }
      })
      .catch((e) => console.log(e));
}

getCommits('EstudoInd');