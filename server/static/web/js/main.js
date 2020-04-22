function Rules(form) {
    if (form.find_order.value > 8000) {form.find_order.value=8000};
    if (form.find_dustbin.value > 100000) {form.find_dustbin.value=100000};
}
