// --- CART --- //
var updateBtns = document.getElementsByClassName('update-cart');
//console.log(user)
for(var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click',(e)=>{
        e.preventDefault();
        //console.log(data)
        var productID = e.target.dataset.product;
        //console.log(productID)
        var sizeId = e.target.dataset.size;
        var action = e.target.dataset.action;
        //console.log("User: ", user)
        //console.log(productID, action)

        addCookieItem(productID, sizeId, action);
          
    })
}
//user not logged in update cookie cart
async function addCookieItem(productID,sizeId,action){
    //console.log("not logged in");
    if(action == 'add'){
        if(cart[productID] == undefined){
            cart[productID] = {'quantity':1,'size_id':sizeId};
        }else{
            cart[productID]['quantity'] += 1;
        }
    }
    if(action == 'remove'){
        cart[productID]['quantity'] -= 1;

        if(cart[productID]['quantity'] <= 0){
            console.log("removed Item")
            delete cart[productID]
        }
    }

    //set cookie
    //console.log('CART:', cart)
    document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"
    
    window.location.reload()
}

function updateCustomerOrder(productID, sizeID, action){

    var url = 'update_item/';

    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken
        },
        body:JSON.stringify({
            'productID':productID, 
            'sizeID': sizeID,
            'action': action
        })
    }).then((res) => {
        return res.json()
    }).then((data) =>{
        console.log(data)
        // once updated reload page
        //location.reload()
    })
    window.location.reload()
}


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
                centerPadding: '40px',
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

//merch tiles
var srcSwap = function () {
    var $this = $(this);
    var newSrc = $this.data('alt-src');
    $this.data('alt-src', $this.attr('src'));
    $this.attr('src', newSrc)
}
$(function (){
    $(".thumbnail").hover(srcSwap,srcSwap)
});
//parallax
window.addEventListener('scroll', throttle(parallax, 14));

function throttle(fn, wait) {
  var time = Date.now();
  return function() {
    if ((time + wait - Date.now()) < 0) {
      fn();
      time = Date.now();
    }
  }
};


