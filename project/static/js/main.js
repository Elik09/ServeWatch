const menuOpen = document.getElementById('menuOpen');
const menuClose = document.getElementById('menuClose');
const menu = document.getElementById('navBar');

const errorBox = document.getElementById('errorBox');

// window.setInterval(()=>{
//     console.log("welcome");
// }, 2000);


menuOpen.addEventListener('click', ()=> {
    menu.classList.add('show--nav');
});

menuClose.addEventListener('click', ()=>{
    menu.classList.remove('show--nav');
});


window.onload =  ()=> {

    if(errorBox !== null){

        setTimeout(()=>{
            errorBox.classList.add('hide--errorBox');
        }, 1000)
    }
    else {
        console.log('nothing to clean')
    }
}