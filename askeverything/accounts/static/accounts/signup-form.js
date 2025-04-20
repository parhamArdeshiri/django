let labels = document.getElementsByTagName("label")
let usernameInput = document.getElementsByName("username")[0], password1Input = document.getElementsByName("password1")[0], password2Input =  document.getElementsByName("password2")[0];
let signupBtn = document.getElementById("signupbtn");

//username part

labels[0].style.position = "absolute";
labels[0].style.top = "255px"
labels[0].style.left = "491px"
labels[0].style.fontSize = "24px"

usernameInput.style.position = "absolute";
usernameInput.style.width = "200px";
usernameInput.style.height = "25px"
usernameInput.style.top = "295px";
usernameInput.style.left = "440px";

//password part

labels[1].style.position = "absolute";
labels[1].style.top = "342px"
labels[1].style.left = "491px"
labels[1].style.fontSize = "24px"

password1Input.style.position = "absolute";
password1Input.style.width = "200px";
password1Input.style.height = "25px"
password1Input.style.top = "382px";
password1Input.style.left = "440px";


//password confirmation part

labels[2].style.position = "absolute";
labels[2].style.top = "430px"
labels[2].style.left = "424px"
labels[2].style.fontSize = "24px"

password2Input.style.position = "absolute";
password2Input.style.width = "200px";
password2Input.style.height = "25px"
password2Input.style.top = "470px";
password2Input.style.left = "440px";

signupBtn.style.position = "absolute";
signupBtn.style.top = "515px";
signupBtn.style.left = "513px";
signupBtn.style.width = "70px";
signupBtn.style.height = "25px";
signupBtn.style.border = "0 solid black";
signupBtn.style.borderRadius = "10px"
signupBtn.style.backgroundColor = "#3498db";