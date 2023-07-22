import { useEffect, useState } from 'react'
import '../../styles/global.css'
import './styles.css'
import { CardPerson, CardProps } from '../../components/CardPerson'
import { HomeHeader } from '../../components/HomeHeader'

type ProfileResponse = {
  name: string;
  avatar_url: string;
}

type User = {
  name:string;
  avatar: string;
}

export default function Home() {
  const [name, setName] = useState('')
  const [names, setNames] = useState<CardProps[]>([])

  const [user, setUser] = useState<User>({} as User)

  function handleNameChange(name: string) {
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

    async function fetchData() {
      const response = await fetch("https://api.github.com/users/guifreitasds")
      const data = await response.json() as ProfileResponse;

      setUser({
        name: data.name,
        avatar: data.avatar_url
      })
    }

    fetchData()
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

