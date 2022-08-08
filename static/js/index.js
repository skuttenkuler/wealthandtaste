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
        console.log("User: ", user)
        console.log(productID, action)

        if(user == 'AnonymousUser'){
            addCookieItem(productID, action)
        }
        else{
            updateCustomerOrder(productID, action)
        }
    })
}
//user not logged in update cookie cart
function addCookieItem(productID, action){
    console.log("not logged in");
    if(action == 'add'){
        if(cart[productID] == undefined){
            cart[productID] = {'quantity':1};
        }else{
            cart[productID]['quantity'] += 1;
        }
    }
    if(action == 'remove'){
        cart[productID]['quantity'] - 1;

        if(cart[productID]['quantity'] <= 0){
            console.log("removed Item")
            delete cart[productID]
        }
    }

    //set cookie
    console.log('CART:', cart)
	document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"
	
	//location.reload()
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

}

