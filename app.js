const menu = document.querySelector('#mobile_menu');
const menuLinks = document.querySelector('nav ul');

// Display Mobile Menu
const mobileMenu = () => {
    menu.classList.toggle('is-active');
    menuLinks.classList.toggle('active');
}

menu.addEventListener('click', mobileMenu)