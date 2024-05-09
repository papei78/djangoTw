const formModal =  document.getElementById('form-modal')
const addBtn  = document.getElementById('open-model-btn')
const cancelBtn  = document.getElementById('cancel-btn')
const backdropElm = document.getElementById('backdrop')




cancelBtn.addEventListener('click', ()=>{
    formModal.classList.add('hidden')
})

addBtn.addEventListener('click',()=>{

    formModal.classList.remove('hidden')
})


window.addEventListener('click', (e)=>{
 

    e.target == backdropElm  ? formModal.classList.add('hidden'): false 
})