$(document).ready(function () {
    $('#submit').click(function(event){
        var count = $('#input').val().length;
        if(count == 0) {
            event.preventDefault();
            $('#input').addClass('input-invalid');
        }
    });
});