$(function() {
    $(document).ready(function() {
      $('#example').DataTable();
    });
});

const openPanel = document.getElementById('openPanel');
const closePanel = document.getElementById('closePanel');
const panel = document.querySelector('.left--panel');
const cardBtns = document.querySelectorAll('.card--btn');


openPanel.addEventListener('click', ()=>{
    panel.classList.add('show--panel');

});

closePanel.addEventListener('click', ()=>{
    panel.classList.remove('show--panel');
});

cardBtns.forEach(btn => {
    btn.addEventListener('click', ()=>{
        panel.classList.remove('show--panel');
    });
});


  