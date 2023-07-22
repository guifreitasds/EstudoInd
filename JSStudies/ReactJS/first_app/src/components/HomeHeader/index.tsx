import './style.css'
import React from 'react'

type HomeProps = {
    title: string;
    name: string;
    src: string;
}

export function HomeHeader(props: HomeProps){

    
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