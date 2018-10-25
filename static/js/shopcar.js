$(document).ready(function () {

    // 判断选中的和所有的复选框是否相等,若相等则其为选中
    var a = $("input[name='fcheck']").length;


    var b = $("input[name='fcheck']:checked").length;
    console.info(b)
    if (b > 0) {
        $("input[name='allcheck']").prop('checked', a == b);

    }
    $('button').click(function () {
        if ($("input[name='fcheck']:checked").length > 0) {
            $('form').submit();
        }
    });

    // console.info($("input[name='allcheck']").prop('checked'));

    //群选框变化的函数
    $("input[name='allcheck']").change(function () {

        var f = $("input[name='allcheck']").prop('checked');
        console.info(f);

        var li = '';
        inputs = $("input[name='fcheck']");
        for (var i = 0; i < inputs.length; i++) {
            li += inputs[i].value + ',';

        }
        inputs.prop('checked', f);
        // console.info(li);
        $.ajax({
            url: '/changeall/',
            method: 'post',
            data: {
                'li': li,
                'flag': f,
            },
            success: function () {

            }
        })
    });
    //单选框变化的时候

    $("input[name='fcheck']").change(function () {


        // console.info($("input[name='fcheck']").length);
        $("input[name='allcheck']").prop('checked', $("input[name='fcheck']").length == $("input[name='fcheck']:checked").length);

        var id = $(this).val();
        // console.info(id);
        var st = $("input[name='fcheck']").prop('checked');


        $.ajax({
            url: '/changeone/',
            method: 'post',
            data: {
                'id': id,
                'st': st,
            },
            success: function () {

            }

        })


    });


});