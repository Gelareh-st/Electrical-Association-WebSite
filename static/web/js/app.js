let nav_item=document.getElementsByClassName("navbar-item");
for (let i=0 ; i<nav_item.length ; i++){
    nav_item[i].onmouseover=function(){
        nav_item[i].style.transform = "scale(1.2)";
    }
    nav_item[i].onmouseout=function(){
        nav_item[i].style.transform = "scale(1)";
    }
}
let mobile_menu_btn=document.getElementById("mobile-menu-btn");
let mobile_menu= document.getElementById("mobile-menu");
let close_menu_btn= document.getElementById("close-mobile-menu");
mobile_menu_btn.onclick=function(){
    mobile_menu.style.width="80vw";
}
close_menu_btn.onclick=function(){
    mobile_menu.style.width="0vw";
}