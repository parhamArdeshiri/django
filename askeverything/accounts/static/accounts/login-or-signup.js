let root = document.querySelector(":root").style;
let loginButton = document.getElementById("loginButton");
let signupButton = document.getElementById("signupButton");
let info = document.getElementById("info");

signupButton.style.display = "none";
signupButton.style.width = "70px";
signupButton.style.height = "25px";
signupButton.style.border = "0 solid black";
signupButton.style.borderRadius = "10px";
signupButton.style.marginLeft = "150px"

signupButton.style.width = "50px";
signupButton.style.height = "20px";
loginButton.style.border = "0 solid black";
loginButton.style.borderRadius = "10px";
loginButton.style.backgroundColor = "white";
loginButton.style.marginLeft = "155px"


function login(){
    root.setProperty("--left", "350px");
    loginButton.style.display = "none";
    signupButton.style.display = "flex";
    info.innerHTML = "First visit in 'askeverything' website?";
    info.style.marginLeft = "60px";
    info.style.marginTop = "177px";
}

function signup(){
    root.setProperty("--left", "720px");
    signupButton.style.display = "none";
    loginButton.style.display = "flex";
    info.innerHTML = "Already have an account in 'askeverything' website?";
    info.style.marginLeft = "55px";
    info.style.marginTop = "132px";
}

signup()