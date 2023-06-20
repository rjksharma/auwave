/* ======================= toggle icon navbar======================*/
let menuIcon = document.querySelector('#menu-icon');
let navbar = document.querySelector('.navbar');

menuIcon.onclick = () => {
    menuIcon.classList.toggle('bx-x');
    navbar.classList.toggle('active');
};

// =====================scroll sections active link====================
let sections = document.querySelectorAll('section');
let navLinks = document.querySelectorAll('header nav a');

window.onscroll = () => {
    sections.forEach(sec => {
        let top = window.scrollY;
        let offset = sec.offsetTop - 150;
        let height = sec.offsetHeight;
        let id = sec.getAttribute('id');

        if (top >= offset && top < offset + height) {
            navLinks.forEach(links => {
                links.classList.remove('active');
                document.querySelector('header nav a[href*=' + id + ']').classList.add('active');

            });
        };
    });
    // =====================sticky navbar ====================
    let header = document.querySelector('header');

    header.classList.toggle('sticky', window.scrollY > 100);

    // =====================remove toggle icon and navbar when ckick link(scroll) ====================
    menuIcon.classList.remove('bx-x');
    navbar.classList.remove('active');

};

// ===================== scroll revel ====================
ScrollReveal({
    // reset: true,
    distance: '80px',
    duration: 2000,
    delay: 200

});

ScrollReveal().reveal('.home-content, .ImageFloatTop, .TextFloatTop, .FormFloatTop, .ButtonFloatTop, .heading', { origin: 'top' });
ScrollReveal().reveal('.home-img, .ImageFloatButtom, .TextFloatButtom, .FormFloatButtom, .ButtonFloatButtom, .services-container, .portfolio-box', {
    origin: 'bottom'
});
ScrollReveal().reveal('.home-content h1, .about-img, .ImageFloatLeft, .TextFloatLeft, .FormFloatLeft, .ButtonFloatLeft', { origin: 'left' });
ScrollReveal().reveal('.home-content p, .about-content,.ImageFloatRight, .TextFloatRight, .FormFloatRight, .ButtonFloatRight', { origin: 'right' });


// =================== typed js=====================
const typed = new Typed('.multiple-text', {
    strings: [,'Web Development', 'App Development', 'Game Development', 'Block Chain Development', 'Ecommerce Solution', 'Digital Marketing'],
    typeSpeed: 100,
    backSpeed: 100,
    backDelay: 1000,
    loop: true
});


// -----------------owlCarousel---------------

$('.brand-carousel').owlCarousel({
    loop: true,
    margin: 10,
    autoplay: true,
    responsive: {
        0: {
            items: 1
        },
        600: {
            items: 3
        },
        1000: {
            items: 5
        }
    }
})

// -----------preloader-------------
var loader = document.getElementById("preloader");

window.addEventListener("load", function () {
    loader.style.display = "none"
})