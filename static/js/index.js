
$(document).ready(function(){

    front_boaed_handle();

    $(window).resize(function(){
        front_boaed_handle();
    });
    $('#header .menu').click(function() {
        if ($('#header .header_item').hasClass('collapsed')) {
            $('#header .header_item').removeClass('collapsed');
            $('#header .header_item').show();
        } else {
            $('#header .header_item').addClass('collapsed');
            $('#header .header_item').hide();
        }
    });

});


function front_boaed_handle() {
    width = $(window).width();
    var div = $('#front_board');
    var h1 = $('#front_board h1');
    var h2 = $('#front_board h2');
    var img = $('#front_board img');
    var height = width / 2.2;
    if (width > 420) {
        div.css('height', height);
        div.css('padding-top',130*(width/1000));
        h1.css('font-size',80*(width/1000));
        h1.css('border-width',7*(width/1000));
        h2.css('font-size',35*(width/1000));
    } else {
        var ratio = 1.3;
        div.css('height', height);
        div.css('padding-top',130*(width/1000) * ratio);
        h1.css('font-size',80*(width/1000) * ratio);
        h1.css('border-width',8*(width/1000) * ratio);
        h2.css('font-size',35*(width/1000) * ratio);   
        h1.css('width',400 *(width/1000) * ratio);    
        $('#header .header_item').addClass('collapsed');
    }    
}