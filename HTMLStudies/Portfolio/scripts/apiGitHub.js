
function getApiGitHub() {
  fetch('https://api.github.com/users/guifreitasds/repos')
    .then(async (res) => {
      if (!res.ok) {
        throw new Error(res.status);
      }

      var data = await res.json();

      // data.map((item) => {
      //   let li = document.createElement('li');

      //   if(item.description==null){
      //       item.description="Sem descrição"
      //   }
      //   li.innerHTML = `
      //   <strong>${item.name} Repo</strong>
      //   <span>${item.description}</span>
      //   <span><a href='${item.html_url}'>Clique aqui para acessá-lo</a> </span>
      //   <span>Data criação: 
      //     ${Intl.DateTimeFormat('pt-BR').format(new Date(item.created_at))}
      //   </span>
      //   `;

      //   ul.appendChild(li);
      // });

      for (let i = 0; i < 6; i++) {
        const item = data[i];
        let divone = document.createElement('div');
        let divproj = document.querySelector('div.projects');

        if(item.description==null){
            item.description="Sem descrição"
        }
        divone.innerHTML = `
        <a class="project-one shadow-box" href="https://github.com/guifreitasds/${item.name}" target="_blank">
          <strong>${item.name}</strong>
          <span>${item.description}</span>
        </a>
        `;

        divproj.appendChild(divone);
        
      }
    })
    .catch((e) => console.log(e));
}

getApiGitHub();