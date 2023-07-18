import { useEffect, useState } from 'react'
import '../../styles/global.css'
import './styles.css'
import { CardPerson } from '../../components/cardPerson'
import { HomeHeader } from '../../components/HomeHeader'

export default function Home() {
  const [name, setName] = useState('')
  const [names, setNames] = useState([])

  const [user, setUser] = useState({name: '', avatar: ''})

  function handleNameChange(name) {
    setName(name);
  }

  function handleAddPerson() {
    const newPerson = {
      name: name,
      time: new Date().toLocaleTimeString("pt-br", {
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit'
      })
    }

    setNames(prevState => [...prevState, newPerson])
  }

  useEffect(()=>{
    // corpo useeffect
    console.log("entrou")
    fetch("https://api.github.com/users/guifreitasds")
      .then(response => response.json())
      .then(data => setUser({
        name: data.name,
        avatar: data.avatar_url
      }))
  }, [])
  return (
    <div className='container'>
      <HomeHeader
        title="Lista de Chamada"
        name={user.name}
        src={user.avatar}
      />
      <input type="text" placeholder='Digite' className='txt' onChange={e => handleNameChange(e.target.value)}/>
      <input type="submit" value="Adicionar" className='btt' onClick={handleAddPerson} autoFocus/>

      {
        names.map(person => (
        <CardPerson
          key={person.time}
          name={person.name} 
          time={person.time}
        />
        )
        )
        
      }
      
    </div>
  )
}

