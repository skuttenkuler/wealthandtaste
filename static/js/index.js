// --- CART --- //
var updateBtns =document.getElementsByClassName('update-cart');

for(var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var productID = this.dataset.product;
        var action = this.dataset.action;
        console.log("User: ", user)
        console.log(productID, action)

        if(user == 'AnonymousUser'){
            console.log("not logged in")
        }
        else{
            updateCustomerOrder(productID, action)
        }
    })
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
    })

}