import './style.css'

export function HomeHeader(props){

    
    return(
        <header>
            <h1>{props.title}</h1>
            <div>
            <strong>{props.name}</strong>
            <img src={props.src} alt="Foto do chamador" />
            </div>
        </header>
    )
}