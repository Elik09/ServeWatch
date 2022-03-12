
const email = document.getElementById('email');

// email verification login

email.addEventListener('keydown', (event)=>{

    let emailReg = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
    if(!emailReg.exec(this.value)){
        // email.nextElementSibling.innerText = "Invalid email format";
        // return
        console.log('error');
    }
    else {
        console.log("success");
        // email.nextElementSibling.innerText = "";
    }
    
});