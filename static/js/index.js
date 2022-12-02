
$(document).ready(function(){
    //Slick Carousel
    $(".tattoo-tiles").slick({
        centerMode: false,
        infinite:false,
        arrows: true,
        prevArrow: '<button class="slide-arrow prev-arrow"></button>',
        nextArrow: '<button class="slide-arrow next-arrow"></button>',
        centerPadding: '60px',
        slidesToShow: 3,
        adaptiveHeight:true,
        responsive: [
            {
            breakpoint: 768,
            settings: {
                arrows: true,
                prevArrow: '<button class="slide-arrow prev-arrow"></button>',
                nextArrow: '<button class="slide-arrow next-arrow"></button>',
                centerMode: false,
                centerPadding: '40px',
                slidesToShow: 1,
                adaptiveHeight:true,
            }
            },
            {
            breakpoint: 480,
            settings: {
                arrows: true,
                centerMode: true,
                centerPadding: '0px',
                slidesToShow: 1,
                adaptiveHeight:true,
            }
            }
        ]
    });
   
    $(window).addEventListener("scroll", function(){
        const parallax = $(".parallax");
        let offset = window.pageYOffset;
        parallax.style.backgroundPositionY = offset * 0.7 + "px"
    })
})

function throttle(fn, wait) {
  var time = Date.now();
  return function() {
    if ((time + wait - Date.now()) < 0) {
      fn();
      time = Date.now();
    }
  }
};


