// --- CART --- //
var updateBtns = document.getElementsByClassName('update-cart');
//console.log(user)
for(var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click',(e)=>{
        e.preventDefault();
        //console.log(e.target.dataset)
        //console.log(data)
        var productID = e.target.dataset.product;
        var action = e.target.dataset.action;
        //console.log("User: ", user)
        //console.log(productID, action)

        if(user == 'AnonymousUser'){
            addCookieItem(productID, action);
            
        }
        else{
            updateCustomerOrder(productID, action);
           
        }
    })
}
//user not logged in update cookie cart
async function addCookieItem(productID, action){
    //console.log("not logged in");
    if(action == 'add'){
        if(cart[productID] == undefined){
            cart[productID] = {'quantity':1};
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
    console.log('CART:', cart)
    document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"
    
    window.location.reload()
}

function updateCustomerOrder(productID, action){

    var url = 'update_item/';

    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken
        },
        body:JSON.stringify({
            'productID':productID, 
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
        centerMode: true,
        infinite:true,
        arrows: true,
        prevArrow: '<button class="slide-arrow prev-arrow"></button>',
        nextArrow: '<button class="slide-arrow next-arrow"></button>',
        centerPadding: '60px',
        slidesToShow: 3,
        responsive: [
            {
            breakpoint: 768,
            settings: {
                arrows: true,
                prevArrow: '<button class="slide-arrow prev-arrow"></button>',
                nextArrow: '<button class="slide-arrow next-arrow"></button>',
                centerMode: true,
                centerPadding: '40px',
                slidesToShow: 3
            }
            },
            {
            breakpoint: 480,
            settings: {
                arrows: true,
                centerMode: true,
                centerPadding: '40px',
                slidesToShow: 1
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


