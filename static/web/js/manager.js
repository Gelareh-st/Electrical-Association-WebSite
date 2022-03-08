
let manage_menu_btn = document.getElementById("manage-menu-btn");
let manage_menu = document.getElementById("side-sec");
manage_menu_btn.onclick = function () {
    if (manage_menu.classList.contains("close")) {
        manage_menu.style.width = "10rem";
        manage_menu_btn.src = "../static/web/img/icons8-close-50.png";
        manage_menu.classList.add("open");
        manage_menu.classList.remove("close");
        document.getElementById("manage-nav").style.display="block";
    }
    else {
        manage_menu.style.width = "0rem";
        manage_menu_btn.src = "../static/web/img/icons8-menu.svg";
        manage_menu.classList.add("close");
        manage_menu.classList.remove("open");
        document.getElementById("manage-nav").style.display="none";

    }
}
let dropdown=document.getElementById("dropdown");
let dropdown_menu=document.getElementById("dropdown-menu");
dropdown.onmouseover=function(){
dropdown_menu.style.display="block";
}
dropdown.onmouseout=function(){
    dropdown_menu.style.display="none";
    }