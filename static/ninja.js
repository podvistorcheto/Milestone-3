$(document).ready(function () {

    $('.sidenav').sidenav();
    $('.collapsible').collapsible();
    $('select').formSelect();
    $('.dropdown-trigger').dropdown();
    $(".datepicker").datepicker({
        format: "dd mmm yyyy",
        yearRange: 3,
        showClearBtn: true,
        i18n: {
            clear: "Clear",
            done: "OK",
            cancel: "Cancel"
        }
    });
});

// get the button
mybutton = document.getElementById("myButton");

// When the user clicks on the button, brings back the top of the app
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}

