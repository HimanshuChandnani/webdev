$(document).ready(()=>{
    //services part
    resize()
    $(window).resize(()=>{
        resize()
    })
    //counter
    let run = false
    $(window).scroll(()=>{
        let height = window.innerHeight;
        if($('#year-num').offset().top >= $(window).scrollTop() && $('#year-num').offset().top - height <= $(window).scrollTop() && !run){
            run = true;
            incriment()
        }
    })
    //set size of hover
    $('.img-hover').width($('.img-hover').siblings().width())
    //slide in
    let run1 = []
    $(window).scroll(()=>{
        let height = window.innerHeight;
        for(i = 0; i < $('.to-right').length; i++){
            if($('.to-right:eq('+i+')').offset().top >= $(window).scrollTop() && $('.to-right:eq('+i+')').offset().top - height <= $(window).scrollTop() && !run[i]){
                run1[i] = true;
                to_right($('.to-right:eq('+i+')'))
            }
        }
    })
    let run2 = []
    $(window).scroll(()=>{
        let height = window.innerHeight;
        for(j = 0; j < $('.to-left').length; j++){
            if($('.to-left:eq('+j+')').offset().top >= $(window).scrollTop() && $('.to-left:eq('+j+')').offset().top - height <= $(window).scrollTop() && !run[j]){
                run2[j] = true;
                to_left($('.to-left:eq('+j+')'))
            }
        }
    })
    //price direction change
    $('.prices:nth-child(odd)').css('background-image', 'linear-gradient(90deg, transparent 30%, #fbf1ea 30%)');
    $('.prices:nth-child(odd) .col-lg-6:nth-child(2)').css('order','-1').removeClass('to-left').addClass('to-right');
    $('.prices:nth-child(odd) .col-lg-6:nth-child(1)').removeClass('to-right').addClass('to-left');
})

function resize(){
    $('.box').width('100%')
    $('.box img').width('100%');
    $('.box').width($('.box img').width());
    $('.box').height($('.box img').height());
    $('.box').height('+=20px');
    console.log(`box: ${$('.box img').width()} ${$('.box img').height()} img: ${$('.box img').width()}`)
    $('.box img').width('80%');
    $('.box > div').width($('.box img').width());
    $('.box > div').height($('.box img').height());
    console.log(`box: ${$('.box > div').width()} ${$('.box > div').height()} img: ${$('.box img').width()}`)
}

function incriment(){
    console.log('run')
    let year = $('#year-num')
    setInterval(() => {
        if(parseInt(year.html()) < 24){
            year.html(parseInt(year.html()) + 1 + ' +');
        }
    }, 140);
    let client = $('#client-num')
    setInterval(() => {
        if(parseInt(client.html()) < 850){
            client.html(parseInt(client.html()) + 1 + ' +');
        }
    }, 2);
}

function to_right(elem){
    elem.animate({
        left: '0',
        opacity: '1',
    },1000)
}
function to_left(elem){
    elem.animate({
        right: '0',
        opacity: '1',
    },1000)
}