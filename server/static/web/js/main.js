function erMsg(id, field) {
    window.addEventListener('load', () => {
        
        const form = document.getElementById(id);
        
        if (field == "find_dustbin") {
            form.find_dustbin.setCustomValidity("Item not found.");
            form.find_dustbin.value="";
            form.find_dustbin.reportValidity();
        }
        else if (field == "find_order") {
            form.find_order.setCustomValidity("Item not found.");
            form.find_order.value="";
            form.find_order.reportValidity();
        }
    })
}


function Rules(form) {
    if(form.find_order && form.find_order.value) {
        const val = form.find_order.value
        if (val <= 0 || val > 8000) {        // Max of Orders
            form.find_order.setCustomValidity("Insert a number between 1 and 8000.");
            form.find_order.value="";
            form.find_order.reportValidity();
        } else {
            form.submit();
        }
    }
    
    else if(form.find_dustbin && form.find_dustbin.value) {
        const val = form.find_dustbin.value
        if (val <= 0 || val > 100000) {    // Max of Dustbins
            form.find_dustbin.setCustomValidity("Insert a number between 1 and 10,000.");
            form.find_dustbin.value="";
            form.find_dustbin.reportValidity();
        } else {
            form.submit();
        }
    }
}
