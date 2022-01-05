$(document).ready(function(){

    // alert('gre');
    increment_value();
    decreament_value();
    remote_cart();
    getTotal();
    SendEmailContactForm();
    // $('.ClickedMessage').on('click', function(){
    //     const message = $('.m').attr('value');

    //     alert(message);
    // });

    // // $(this).click(function(){
    // //     alert('yh');
    // // });



});


function increment_value(){
    $('.up').click(function (){
        var id = $(this).data('id');
        var price = $(this).data('price');

        var quantity = $('#'+id+'').val();
        quantity = parseInt(quantity) + 1;

        $('#'+id+'').val(quantity);
        $('#phone_cart_quantity'+id+'').html(quantity);
        $('#side_cart_quantity'+id+'').html(quantity);

        increment_cart(id);
        var total = price * quantity
        $('#total'+id+'').html(total.toLocaleString());
        $('#total_amount_phone_cart'+id+'').html(total.toLocaleString());
        getTotal();
    });
}
function decreament_value(){
    $('.down').click(function (){
        var id = $(this).data('id');
        var price = $(this).data('price');

        var quantity = $('#'+id+'').val();
        if (quantity > 1){
            quantity = parseInt(quantity) - 1;
            $('#'+id+'').val(quantity);
            $('#phone_cart_quantity'+id+'').html(quantity);
            $('#side_cart_quantity'+id+'').html(quantity);
        }

        decrement_cart(id);
        var total = price * quantity
        $('#total'+id+'').html(total.toLocaleString());
        $('#total_amount_phone_cart'+id+'').html(total.toLocaleString());
        getTotal();

    });
}

function increment_cart(id){
    $.ajax({
        url: '/cart/increment/'+id+' ',

        dataType: 'json',
        success: function (response) {
            var msg = response.message
            if (msg == "success"){
                getTotal();
            }

        }
    });
}
function decrement_cart(id){
    $.ajax({
        url: '/cart/decrement/'+id+' ',

        dataType: 'json',
        success: function (response) {
            if (response.message = 's') {

            }
        }
    });
}

function remote_cart(){
    $('.clear-cart').click(function (){
        if ( confirm("are you sure?") ){

            var id = $(this).data('id');

            $.ajax({
                url: '/cart/clear/'+id+' ',

                dataType: 'json',
                success: function (response) {
                    if (response.message = 'success') {
                        location.reload();
                    }
                }
            });
        }

    });

}
function getTotal(){
    var total_amount = 0
    $('.total_amount').each(function(i, obj) {
        var total =$(this).html();
        var a = parseInt(total.replace(/,/g, ""))
        var b = parseInt(total_amount)
        var t = b + a;
        total_amount = t;
        // alert(t);

    });
    $('#subtotal').html(total_amount);
    $('#side_cart_total').html(total_amount);
    $('#phone_cart_total').html(total_amount);
    // alert(total_amount);

}


function SendEmailContactForm(){
    $('#contact_form').submit(function(e) {
        e.preventDefault();
        var csrftoken = $("[name=csrfmiddlewaretoken]").val();

        const formdata = $(this).serialize();
        // $('form').serialize()
        $.ajax({
            url: '/contact-us',
            type : "POST",
            headers:{
                "X-CSRFToken": csrftoken
            },
            data: formdata,
            // dataType: 'json',
            success: function (response) {
                if (response.message == 1){
                    $("#contact_form").trigger('reset');
                    $('#Email_message').slideDown(1000,'swing',function(){
                        setTimeout(function() {
                            $('#Email_message').slideUp(1000);
                        }, 4000);
                    })
                }
            }
        });
    });
}