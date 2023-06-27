const button = document.getElementById('openModal');

const divModal = document.querySelector(".modal-wrapper");

function openingModal() {
    divModal.classList.remove("invisible")
}


document.addEventListener("keydown", (e)=>{
    if(e.key=="Escape" && divModal.classList[1]!="invisible"){
        divModal.classList.add("invisible");
    };

})

