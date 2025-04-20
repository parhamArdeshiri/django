let label = document.getElementsByTagName("label")[0];
let input = document.getElementsByName("name")[0];
let createbtnfc = document.getElementById("createbtnfc");

label.style.position = "absolute";
label.style.left = "666px";
label.style.top = `${document.getElementsByTagName("h4").length * 73 + 5}px`;
label.style.fontSize = "15px";

input.style.position = "absolute";
input.style.left = "648px";
input.style.top = `${document.getElementsByTagName("h4").length * 73 + 26}px`;
input.style.width = "75px";
input.style.height = "26px";
input.style.backgroundColor = "rgb(180, 180, 180)";
input.style.border = "1px solid black";
input.style.borderRadius = "10px";

createbtnfc.style.position = "absolute";
createbtnfc.style.left = "662px";
createbtnfc.style.top = `${document.getElementsByTagName("h4").length * 73 + 60}px`;
createbtnfc.style.backgroundColor = "rgb(180, 180, 180)";
createbtnfc.style.border = "1px solid black";
createbtnfc.style.borderRadius = "10px";