import { useState } from 'react'
import '../../styles/global.css'
import './styles.css'


export default function Home() {
  const [count, setCount] = useState(0)

  return (
    <div className='container'>
      <h1>App de lista de tarefas</h1>
      <input type="text" placeholder='Digite' className='txt'/>
      <input type="submit" value="Enviar" className='btt'/>
    </div>
  )
}

