$(document).ready(function () {

        $('#btn').click(function () {
            ahtml = $('#a').html();
            bhtml = $('#b').html();
            chtml = $('#c').html();
            psw1 =$("input[name='psw1']").val();
            psw2 =$("input[name='psw2']").val();

            if('用户可以使用' == ahtml && psw1 ==psw2 && chtml=='√' ){
                document.forms[0].submit();
            }
        }) ;



        $("input[name='name']").blur(function () {
            uname = $("input[name='name']").val();
            if(uname.length>=6){
               $.ajax({
                    url:'/nameyjy/',
                    method:'GET',
                    data:{'uname':uname},
                    success:function (result) {
                        // alert(result.res);
                        if(result.res=='0001'){
                           $('#a').html('用户名已存在');
                           $('#a').css('color','red')
                        }else{
                            $('#a').html('用户可以使用');
                            $('#a').css('color','green')
                        }
                    }
                })
            }else{
               $('#a').html('请输入不小于6位的用户名');
            }
        });

        $("input[name='psw2']").blur(function () {
            psw1 =$("input[name='psw1']").val();
            psw2 = $("input[name='psw2']").val();

            if(psw1==psw2){
                $('#b').html('√');
                $('#b').css('color','green');

            }else{
                $('#b').html('X');
                $('#b').css('color','red');

            }

        });


        $("input[name='code']").change(function () {
            code = $("input[name='code']").val();
            if(code.length=4){
               $.ajax({
                    url:'/codejy/',
                    method:'GET',
                    data:{'code':code},
                    success:function (result) {
                        if(result.msg=='0000'){
                           $('#c').html('√');
                           $('#c').css('color','green')
                        }else{
                            $('#c').html('X');
                            $('#c').css('color','red')
                        }
                    }
                })
            }
        });




















});