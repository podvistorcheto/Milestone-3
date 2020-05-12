function validate(){
    var email = document.getElementById("email");
    var username = document.getElementById("username");
    var password = document.getElementById("password");

    if(username.value =="" || password.value =="" || email.value =="")
    {
        return("No blank values allowed!");
    }
    else
    {
    }
}