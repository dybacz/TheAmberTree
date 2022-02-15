$(document).ready(function() {
    $("a.nav-link").each(function() {
        if (this.href == window.location.href) {
            $(this).addClass("active");
        } 
    });
    if ($("#booking-link").hasClass("active") === false){
        $("#about-link").addClass("active")
        console.log("err")
    }
    
    let windowHeight = window.innerHeight
    let scrollDemo = document.documentElement
    document.addEventListener("scroll", event => {
        let x = scrollDemo.scrollTop

        if (x < windowHeight/2) {
            $("#about-link").addClass("active")
            $("#menu-link").removeClass("active")
        }
        if (x > windowHeight/2 && x < (3/2)*windowHeight) {
            $("#about-link").removeClass("active")
            $("#drinks-link").removeClass("active")
            $("#menu-link").addClass("active")
        }
        if (x > (3/2)*windowHeight && x < (5/2)*windowHeight){
            $("#menu-link").removeClass("active")
            $("#contact-link").removeClass("active")
            $("#drinks-link").addClass("active")  
        }
        if (x >= (5/2)*windowHeight){
            $("#drinks-link").removeClass("active")
            $("#contact-link").addClass("active")
        }
    }, { passive: true });
});