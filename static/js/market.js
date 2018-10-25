$(document).ready(function () {

    $('#allspan').click(function () {
        $('#allspanlist').show();
        $(this).removeClass('glyphicon glyphicon-chevron-down').addClass('glyphicon glyphicon-chevron-up')
    });
    $('#zhspan').click(function () {
        $('#zhspanlist').show();
        $(this).removeClass('glyphicon glyphicon-chevron-down').addClass('glyphicon glyphicon-chevron-up')
    });
    $('#allspanlist').click(function () {
        $('#allspanlist').hide();
        $('#allspan').removeClass('glyphicon glyphicon-chevron-up').addClass('glyphicon glyphicon-chevron-down')
    });
    $('#zhspanlist').click(function () {
        $('#zhspanlist').hide();
        $('#zhspan').removeClass('glyphicon glyphicon-chevron-up').addClass('glyphicon glyphicon-chevron-down')
    });

    $('.addShopping').click(function () {
        goodid = $(this).val();
        // alert(goodid );
        span = $(this).prev();
        $.ajax({
            url: '/addshopcar/',
            method: 'GET',
            data: {'goodid': goodid},
            success: function (obj) {
                if (obj.result == '0000') {
                    span.html(obj.num)
                } else {
                    // 说明没登录，跑到登录页面
                    window.open('/login/', '_self')
                }
            }
        });

    });

    $('.subShopping').click(function () {
        goodid = $(this).val();
        alert(goodid );
        span = $(this).next();
        $.ajax({
            url: '/subshopcar/',
            method: 'GET',
            data: {'goodid': goodid},
            success: function (obj) {
                if(obj.result=='0001'){
                   // 说明没登录，跑到登录页面
                    window.open('/login/', '_self')
                }else{
                    span.html(obj.num)
                }

            }
        });

    });


});