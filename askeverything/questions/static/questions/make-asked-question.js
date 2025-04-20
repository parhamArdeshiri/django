function moveByName(x, y, name) {
    let element = document.getElementsByName(name)[0];

    element.style.position = "absolute";
    element.style.left = `${x}px`;
    element.style.top = `${y}px`;

}


let labels = document.getElementsByTagName("label");
let title = document.getElementsByName("title");
let text = document.getElementsByName("text");
let categoryField = document.getElementsByTagName("select")[0];

labels[0].style.position = "absolute";
labels[0].style.left = "670px";
labels[0].style.top = "165px";
labels[0].style.fontSize = "20px";

labels[1].style.position = "absolute";
labels[1].style.left = "690px";
labels[1].style.top = "240px";
labels[1].style.fontSize = "20px";

labels[2].style.position = "absolute";
labels[2].style.left = "690px";
labels[2].style.top = "315px";
labels[2].style.fontSize = "20px";

title[0].style.width = "245px";
title[0].style.height = "25px";
title[0].style.border = "1px solid #ccc";
title[0].style.borderRadius = "10px";

text[0].style.width = "400px";
text[0].style.height = "225px";
text[0].style.borderRadius = "10px";
text[0].style.border = "1px solid #ccc";

categoryField.style.width = "110px";
categoryField.style.height = "27px";
categoryField.style.borderRadius = "10px"

moveByName(580, 280, "title");
moveByName(512, 355, "text");
moveByName(660, 207, "category");

