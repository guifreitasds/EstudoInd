import { useState } from 'react'
import '../../styles/global.css'
import './styles.css'
import { CardPerson } from '../../components/cardPerson'

export default function Home() {
  const [name, setName] = useState('')

  function handleNameChange(name) {
    setName(name);
  }

  return (
    <div className='container'>
      <h1>App de lista de Presença</h1>
      <input type="text" placeholder='Digite' className='txt' onChange={e => handleNameChange(e.target.value)}/>
      <input type="submit" value="Enviar" className='btt'/>

      <CardPerson name={name} time="10:20:40"/>
      <CardPerson name="Rodrigo Gonçalves" time="10:25:10"/>
      <CardPerson name="Carlos Alberto" time="11:05:38"/>
    </div>
  )
}

