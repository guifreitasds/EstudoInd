import './style.css'

export function CardPerson(props) {
    
    return(
        <div className='container-card'>
            <strong>{props.name}</strong>
            <small>{props.time}</small>
        </div>
    )
}