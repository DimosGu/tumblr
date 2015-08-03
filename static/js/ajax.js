function get_blog() {

	$.ajax({
		url: "blogs/post",
		type: "POST",
		data: { 
			images: ????,
		},

		success: function(error) {
			
		},

		error: function() {
			form_error_id.html('<p>There was a form error.</p>');
		}
	});
}