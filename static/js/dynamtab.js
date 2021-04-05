function addingrow(){
     {% block content %}
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script>
$(document).ready(function(){
    setTimeout(function(){
       location.reload(true);
       alert("The page will now refresh");
    }, 60000);
});
</script>
{% endblock content %}}


$("body").delegate('#remove','click',function()
		{
			$(this).parent().parent().remove();
		});
