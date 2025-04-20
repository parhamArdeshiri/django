function moveByID(x, y, name) {
    let element = document.getElementById(name);

    element.style.position = "absolute";
    element.style.left = `${x}px`;
    element.style.top = `${y}px`;

}

let q = document.getElementsByClassName("Q");
let element = document.getElementsByName("text")[0];
let addbtn = document.getElementById("addbtn");
let label = document.getElementsByTagName("label")[0];

q[0].style.position = "absolute";
q[0].style.left = "455px";
q[0].style.top = "64px";

element.style.width = "500px";
element.style.height = "200px";
element.style.position = "absolute";
element.style.left = "445px";

element.style.top = `${element.getBoundingClientRect().top - document.body.getBoundingClientRect().top + 50}px`;
element.style.borderRadius = "10px";
element.style.backgroundColor = "rgb(180, 180, 180)"

label.style.position = "absolute";
label.style.left = "695px";
label.style.fontSize = "20px";

addbtn.style.position = "absolute";
addbtn.style.left = "695px";
addbtn.style.top = `${element.getBoundingClientRect().top - document.body.getBoundingClientRect().top + 225}px`
addbtn.style.width = "60px";
addbtn.style.height = "25px";
addbtn.style.backgroundColor = "rgb(180, 180, 180)";
addbtn.style.borderRadius = "10px";
addbtn.style.border = "1px solid black";

moveByID(480, -14, "title");
moveByID(694, 20, "text");