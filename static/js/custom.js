$(document).ready(function(){
  $("#info_form").on('submit', function(e){
    console.log("Info info");
    e.preventDefault();
    var $pincode = $('#pincode').val();
    var $money = $('#money').val();
    $.ajax({
      dataType: "json",
      url: '/api/servicedata/',
      data: {pincode: $pincode, money_limit__gt: $money, format: 'json', order_by: 'priority'},
      type: 'GET',
      success: function(data){
        $("select").remove();
        var $dropdown = "<select>";
        if(data.objects.length > 0)
        {
          $.each(data.objects, function(key, value) {
            $dropdown = $dropdown + "<option>" + value.company_name + "</option>";
          });
        }
        else
        {
          $dropdown = $dropdown + "<option>" + "No Service" + "</option>";
        }
        $dropdown = $dropdown + "</select>";
        $("#info_form").append($dropdown);
      }
    });
  });
});
