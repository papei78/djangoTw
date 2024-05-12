const head = document.getElementById('head')



if(head){

    const goBackBtn = document.getElementById('go-back-btn')
    // the question mark is to verify that the variable is not null nor undefined
    goBackBtn?.addEventListener('click',()=>{
        history.back()
    })
}