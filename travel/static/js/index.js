const login = document.querySelector('.loginNew');
const signin = document.querySelector('.createAccountNew');


document.querySelector('.createAccount').addEventListener('click', (e) => {
    e.preventDefault()
    signin.classList.remove('Fhidden');
    login.classList.add('Fhidden');
})

document.querySelector('.loginNow').addEventListener('click', (e) => {
    e.preventDefault()
    login.classList.remove('Fhidden');
    signin.classList.add('Fhidden');
})

// This is for Login page ---------------
// let user = document.getElementById('username');
// let pass = document.getElementById('password');





//   This is for signup page----------------
let user = document.getElementById('username');
let email = document.getElementById('email');
let pass = document.getElementById('password');
let mpass = document.getElementById('mpassword');


user.addEventListener('blur', () => {
    console.log('This is blur right now');
    let regx = /^[a-zA-Z]([0-9a-zA-Z]){4,12}/;
    str = user.value;
    console.log(regx, str);
    if (regx.test(str)) {
        console.log('It matched');
        user.classList.remove('Finput--error');
    }
    else {
        console.log('It is not matched');
        user.classList.add('Finput--error');
    }


})

email.addEventListener('blur', () => {
    let regx = /^([_\-\0-9a-zA-Z]+)@([_\-\0-9a-zA-Z]+)\.([a-zA-Z]){2,7}$/;
    str = email.value;
    console.log(regx, str)
    if (regx.test(str)) {
        console.log('Email matched');
        email.classList.remove('Finput--error');
    }
    else {
        console.log('You have got some error in Email');
        email.classList.add('Finput--error');
    }
})

pass.addEventListener('blur', () => {
    let regx = /^[A-Za-z]\w{7,14}$/;
    str = pass.value;
    console.log(regx, str);
    if (regx.test(str)) {
        console.log('Password varify');
        pass.classList.remove('Finput--error');
    }
    else {
        console.log('You have got some problem in password');
        pass.classList.add('Finput--error');
    }
});

mpass.addEventListener('blur', () => {
    let regx = /^[A-Za-z]\w{7,14}$/;
    str = mpass.value.match(pass);
    if (regx != str) {
        console.log('Error');
    }
    else {
        console.log('Your password has been matched');
    }

});
