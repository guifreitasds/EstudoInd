import './style.css'

export type CardProps = {
    name: string;
    time: string;
}

export function CardPerson(props: CardProps) {
    
    return(
        <div className='container-card'>
            <strong>{props.name}</strong>
            <small>{props.time}</small>
        </div>
    )
}