$(document).ready(function(){
	$('#submit').click(function(){
		$.post('/polls/details/',{
			day : $('#day_input').val(),
			cost : $('#cost_input').val(),
			remarks : $('#remarks_input').val()
		});
	});
});