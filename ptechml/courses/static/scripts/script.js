let header = document.querySelector('.header-wrap');
let headerOnScroll = function () {
    if (pageYOffset === 0) {
        header.classList.add('header-light');
    }
    else{
        header.classList.remove('header-light');
    }
}
window.addEventListener('scroll', headerOnScroll);

// 
// 
// 

let header__user = document.querySelector('.header__user');
let header__dropdown = document.querySelector('.header__dropdown');
let onHeaderUserHover = function () {
    header__user.classList.add('header__user-active');
    header__dropdown.classList.remove('dn');
}
let onHeaderUserMouseLeave = function () {
    header__user.classList.remove('header__user-active');
    header__user.removeEventListener('mouseenter', onHeaderUserHover);
    header__user.removeEventListener('mouseleave', onHeaderUserMouseLeave);
    setTimeout(function(){
        header__dropdown.classList.add('dn');
        header__user.addEventListener('mouseenter', onHeaderUserHover);
        header__user.addEventListener('mouseleave', onHeaderUserMouseLeave);
    }, 300)
}
header__user.addEventListener('mouseenter', onHeaderUserHover);
header__user.addEventListener('mouseleave', onHeaderUserMouseLeave);