$(document).ready(function(){
   $('#login').click(function(){
        $.post('/polls/login/',{
          username : $('#username').val(),
          password : $('#password').val()
        },function(results){
          console.log(results);
          if(results['success']){
            alert('login success')
            //location = 'http://www.baidu.com';
          }else{
            alert(results['reason']);
          }
        });
      });


})