
const emailRegex = /^\S+@\S+\.\S+$/;
const passwordRegex = /^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$/;
const ipRegex = /^(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/;


if(emailInput !== null){
    emailInput.addEventListener("keyup", ()=>{

        if(emailRegex.test(emailInput.value)){
    
            emailInput.classList.remove('error--outline')
            emailInput.nextElementSibling.innerText = "";
        }
        else {
            emailInput.classList.add('error--outline')
            emailInput.nextElementSibling.innerText = "Invalid email format";
        }
    })

}

if(passwordInput !== null){
    passwordInput.addEventListener("keyup", ()=>{

        if(passwordRegex.test(passwordInput.value)){
        
            passwordInput.classList.remove('error--outline')
            passwordInput.nextElementSibling.innerText = "";
        }
        else {
            passwordInput.classList.add('error--outline')
            passwordInput.nextElementSibling.innerText = "weak password";
        }
        })
}

if(passwordConfInput !== null){
    passwordConfInput.addEventListener("keyup", ()=>{

    if(passwordRegex.test(passwordConfInput.value)){
    
        passwordConfInput.classList.remove('error--outline')
        passwordConfInput.nextElementSibling.innerText = "";
    }
    else {
        passwordConfInput.classList.add('error--outline')
        passwordConfInput.nextElementSibling.innerText = "weak password";
    }
    })
}

if(ipInput !== null){
    ipInput.addEventListener("keyup", ()=>{

    if(ipRegex.test(ipInput.value)){
    
        ipInput.classList.remove('error--outline')
        ipInput.nextElementSibling.innerText = "";
    }
    else {
        ipInput.classList.add('error--outline')
        ipInput.nextElementSibling.innerText = "IPV4 formart allowed!";
    }
    })
}



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