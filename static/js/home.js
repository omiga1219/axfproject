
$(document).ready(function () {

    var myswiper1 = new Swiper('#topSwiper',{

        autoplay:2000,

        // 如果需要分页器
        pagination:'.swiper-pagination',

    });
    var myswiper2 = new Swiper('#swiperMenu',{



        // 分页展示，一页几条
        slidesPerView: 3,

    });


});