function moveByID(x, y, name) {
    let element = document.getElementById(name);

    element.style.position = "absolute"; 
    element.style.left = `${x}px`;
    element.style.top = `${y}px`;

}

function moveByClassName(x, y, className) {
    let Class = document.getElementsByClassName(className)[0];

    Class.style.position = "absolute";
    Class.style.left = `${x}px`;
    Class.style.top = `${y}px`;
}

moveByID(7, -20, "title");
moveByID(246, 7, "text");

// moveByClassName(7, 64, "Q")

let lines = document.getElementsByClassName("line");

for(let i = 0;i<lines.length;i++){
    lines[i].style.position = "absolute";
    lines[i].style.fontSize = "48px";
    lines[i].style.width = "560px";
    lines[i].style.left = "50px";
    lines[i].style.top = "30px";
}
