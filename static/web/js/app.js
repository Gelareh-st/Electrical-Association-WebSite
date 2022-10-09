let nav_item = document.getElementsByClassName("navbar-item");
for (let i = 0; i < nav_item.length; i++) {
  nav_item[i].onmouseover = function () {
    nav_item[i].style.transform = "scale(1.2)";
  }
  nav_item[i].onmouseout = function () {
    nav_item[i].style.transform = "scale(1)";
  }
}
let mobile_menu_btn = document.getElementById("mobile-menu-btn");
let mobile_menu = document.getElementById("mobile-menu");
let close_menu_btn = document.getElementById("close-mobile-menu");
mobile_menu_btn.onclick = function () {
  mobile_menu.style.width = "80vw";
}
close_menu_btn.onclick = function () {
  mobile_menu.style.width = "0vw";
}


// var fade = setInterval(function(){fading()} , 100)



// ////////////////////////////////////////////////////////////////
var slides = document.getElementsByClassName("slide");
var slidesLenght = slides.length * -16;
slidesLenght+=16;
// alert(slidesLenght)
var mRight = 0;

var list =document.getElementById("slider");
function slideLeft() {
  list.appendChild(list.firstElementChild);

}
function slideRight() {
  list.insertBefore(list.lastElementChild,list.firstElementChild);
}
