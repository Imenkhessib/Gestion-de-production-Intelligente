document.addEventListener('DOMContentLoaded', function () {
   $('.plan3d').removeAttr("required");

   $(document).on('change', '.machine_choices', function(){
      if(this.checked) {
         $('.machine_choices').removeAttr('required');
      }
      else if (!$('.machine_choices').is(':checked')){
      $('.machine_choices').prop('required',true);
      }
   });


    $(document).on('change', '.machine_choices', function(){

      if ($(this).attr("value")=== "cnc") {
         if(this.checked){
             $('.plan3d').attr('required',true);
         }
         else{
             $('.plan3d').attr('required',false);
         }
      }
      else if($(this).attr("value")=== ""){
          $('.plan3d').removeAttr('required');
      }
   });

});