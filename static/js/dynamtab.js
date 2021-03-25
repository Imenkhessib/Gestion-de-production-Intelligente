function addingrow(){
    var tab1= document.getElementById("itemstab");
    var row = tab1.insertRow();
    var td1 = row.insertCell();
    var cell2ref = row.insertCell ();
    var cell2desig = row.insertCell ();
    var cell3qty = row.insertCell ();
    var cell4delete = row.insertCell ();
    var cell5browse = row.insertCell ();

    td1.className = "count";
    cell2ref .innerHTML = document.getElementById("ref").value;
    cell2desig.innerHTML = document.getElementById("desig").value;
    cell3qty.innerHTML = document.getElementById("quantity").value;
    cell4delete.innerHTML = '<input type="button" class="btn btn-outline-primary" id="remove" value="Delete Row">';
}


$("body").delegate('#remove','click',function()
		{
			$(this).parent().parent().remove();
		});
