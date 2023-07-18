import { useState } from 'react'
import '../../styles/global.css'
import './styles.css'
import { CardPerson } from '../../components/cardPerson'
import { HomeHeader } from '../../components/HomeHeader'

export default function Home() {
  const [name, setName] = useState('')
  const [names, setNames] = useState([])

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

  return (
    <div className='container'>
      <HomeHeader
        title="Lista de Chamada"
        name="Guilherme"
        src="https://github.com/guifreitasds.png"
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

