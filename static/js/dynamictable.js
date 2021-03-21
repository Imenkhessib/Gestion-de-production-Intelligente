$(function()
	{
      // Add Row
		$("#addrow").click(function()
		{
			addnewrow();
		});

      // Remove Row
      	$("body").delegate('#remove','click',function()
		{
			$(this).parent().parent().remove();
		});

    });
	function addnewrow()
	{
		var tr = '<tr>'+
                          '<td class="count"></td>'+
                          '<td></td>'+
                          '<td></td>'+
                          '<td></td>'+
                          '<td><input type="button" class="btn btn-outline-primary" id="remove" value="Delete Row" > </td>'+
                  '</tr>'
		$(".detail").append(tr);
	}