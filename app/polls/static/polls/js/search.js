$(document).ready(function(){
	$('#search').click(function(){
		$.post('',{
			search_mouth : $('#search_mouth').val()
		},function(results){
			console.log(results);
			if(results['login']){ 
				if(results['success']){
					if(results['data']){
						$('p').remove();
						$('body').append('<p>'+results['mouth']+'</p>');
						$('body').append('<p>'+results['day']+'</p>');
						$('body').append('<p>'+results['cost']+'</p>');
						$('body').append('<p>'+results['remarks']+'</p>');
						$('body').append('<p>'+results['residu']+'</p>');
					}else{
						$('p').remove();
						$('body').append('<p>'+results['back']+'</p>');
					}
				}else{
					$('p').remove();
					$('body').append('<p>'+results['back']+'</p>')
				}
			}else{
				location = '/polls/login/';
			}
		});
	});
});