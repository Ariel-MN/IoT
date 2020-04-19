function Preview(form) {
    var dustbins = form.dustbins_upd.value;
    if (dustbins != "") {dustbins= '('+dustbins+')'} else {dustbins=""};
    if (form.employee_upd.value != "Employee ID") {var employee = form.employee_upd.value} else {employee=""};
    if (form.number_upd.value > 8000) {form.number_upd.value=8000};
    var number = form.number_upd.value;
    var date = form.date_upd.value;

    document.getElementById("number-upd").innerHTML = '# ' + number;
    document.getElementById("employee-upd").innerHTML = 'Employee Id: ' + employee;
    document.getElementById("dustbins-upd").innerHTML = 'Dustbins: ' + dustbins;
    document.getElementById("date-upd").innerHTML = 'Harvest Date: ' + date;
}