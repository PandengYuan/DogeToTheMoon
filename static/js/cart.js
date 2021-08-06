

// the function used to calculate the total price of choosen products
function calculate_price(obj){

    if(obj.checked){

        var arr = obj.parentNode.children;
        var index = 0;
        for (var i = 0 ; i < arr.length; i++){
            if (arr[i].id == 'price') {
                index = i;
                break;
            }
        }

        // the specific price of a kind of product
        var price = parseFloat(obj.parentNode.children[index].innerHTML);

        // total price
        var total_price = parseFloat(document.getElementById("total_price").innerHTML);
      
        // pass the total price to the destination object
        //document.getElementById("total_price").innerHTML = total_price + price

    }
    
    
}