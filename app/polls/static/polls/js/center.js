$(document).ready(function(){
	$('#btn_submit').click(function(){
		$.post('/polls/center/',{
			day : $('#add_day').val(),
			cost : $('#add_cost').val(),
			remarks : $('#add_remarks').val()
		},function(results){
			if(results['success']){
				location = '/polls/search/';
			}
		});
	});
});