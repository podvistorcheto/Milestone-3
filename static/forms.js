$(document).ready(function(){
    $("#myBtn").click(function(){
        var isValid = true;
        if ($("#upload-date").val() == ""){
            isValid = false;
        }
        if ($("#upload-date").val() == null){
            isValid = false;
        }
        if(isValid == false){
            alert("Please enter valid input in all required fields");
        }
  });
});

