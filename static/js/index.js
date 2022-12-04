
$(document).ready(function(){
    //Slick Carousel
    $(".tattoo-tiles").slick({
        centerMode: false,
        infinite:false,
        arrows: true,
        prevArrow: '<button class="slide-arrow prev-arrow"><svg class="slideshow-arrow" width="23" height="39" viewBox="0 0 23 39" style="transform: scaleX(-1) scale(1);"><path d="M857.005,231.479L858.5,230l18.124,18-18.127,18-1.49-1.48L873.638,248Z" fill=var(--primary) transform="translate(-855 -230)"></path></svg></button>',
        nextArrow: '<button class="slide-arrow next-arrow"><svg style="transform:scaleX(1) scale(1);fill:" width="23" height="39" viewBox="0 0 23 39"><path d="M857.005,231.479L858.5,230l18.124,18-18.127,18-1.49-1.48L873.638,248Z" fill=var(--primary) transform="translate(-855 -230)"></path></svg></button>',
        centerPadding: '60px',
        slidesToShow: 3,
        adaptiveHeight:true,
        responsive: [
            {
            breakpoint: 768,
            settings: {
                arrows: true,
                prevArrow: '<button class="slide-arrow prev-arrow"><svg class="slideshow-arrow" width="23" height="39" viewBox="0 0 23 39" style="transform: scaleX(-1) scale(1);"><path d="M857.005,231.479L858.5,230l18.124,18-18.127,18-1.49-1.48L873.638,248Z" fill=var(--primary) transform="translate(-855 -230)"></path></svg></button>',
                nextArrow: '<button class="slide-arrow next-arrow"><svg style="transform:scaleX(1) scale(1);fill:" width="23" height="39" viewBox="0 0 23 39"><path d="M857.005,231.479L858.5,230l18.124,18-18.127,18-1.49-1.48L873.638,248Z" fill=var(--primary) transform="translate(-855 -230)"></path></svg></button>',
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
              prevArrow: '<button class="slide-arrow prev-arrow"><svg class="slideshow-arrow" width="23" height="39" viewBox="0 0 23 39" style="transform: scaleX(-1) scale(1);"><path d="M857.005,231.479L858.5,230l18.124,18-18.127,18-1.49-1.48L873.638,248Z" fill=var(--primary) transform="translate(-855 -230)"></path></svg></button>',
              nextArrow: '<button class="slide-arrow next-arrow"><svg style="transform:scaleX(1) scale(1);fill:" width="23" height="39" viewBox="0 0 23 39"><path d="M857.005,231.479L858.5,230l18.124,18-18.127,18-1.49-1.48L873.638,248Z" fill=var(--primary) transform="translate(-855 -230)"></path></svg></button>',
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


