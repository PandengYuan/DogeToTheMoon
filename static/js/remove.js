


function remove(){

    var arr = document.getElementsByName('item');
    
    //alert(arr[0].checked)
    for(var i = 0; i < arr.length; i++){

        if(arr[i].checked){

            arr[i].parentNode.parentNode.parentNode.remove();

        }

    }
       

        
    
    
}