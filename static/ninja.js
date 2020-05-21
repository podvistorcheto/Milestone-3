$(document).ready(function () {

    $('.sidenav').sidenav();
    $('.collapsible').collapsible();
    $('select').formSelect();
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
