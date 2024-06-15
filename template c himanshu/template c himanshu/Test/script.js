function active(elem){
    document.getElementById('a1').classList.remove('active');
    document.getElementById('a2').classList.remove('active');
    document.getElementById('a3').classList.remove('active');
    document.getElementById('a4').classList.remove('active');
    document.getElementById('a5').classList.remove('active');
    document.getElementById('a6').classList.remove('active');
    document.getElementById('a7').classList.remove('active');
    document.getElementById('a8').classList.remove('active');
    elem.classList.add('active');
    if(document.location.hash){
        setTimeout(function() {
            window.scrollTo(window.scrollX, window.scrollY - 69.4);
        }, 30);
    }
}
