const openSideBar = document.getElementById('openSide');
const closeSideBar =document.getElementById('closeSide');
const sideBar = document.querySelector('.left--section');

openSideBar.addEventListener('click', ()=>{

    sideBar.classList.add('open--sideBar');
});

closeSideBar.addEventListener('click', ()=>{
    sideBar.classList.remove('open--sideBar')
});