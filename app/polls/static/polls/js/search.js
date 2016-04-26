$(document).ready(function(){
	$('#search').click(function(){
		$.post('',{
			search_mouth : $('#search_mouth').val()
		},function(results){
			console.log(results);
			if (results['success']){ 
				$('.mouth_show').html(results['mouth']);
				$('.time').html(results['day']+':'+results['cost']);
				$('.remarks').html(results['remarks']);
			}else{
				location = '/polls/login/';
			}
		});
	});
});