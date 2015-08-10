$('body').on('click', '.blog-footer-options', function() {
	var footer_options = $(this).find('.options-popup');

	if (footer_options.hasClass('display-none')) {

		setTimeout (function() {
			footer_options.removeClass('display-none');		

			if(footer_options.offset().top - $(window).scrollTop() >= 
				window.innerHeight - footer_options.height() - 22) {
				footer_options.addClass('popup-high');
			} else {
				footer_options.addClass('popup-low');
			}
		}, 1);
	}
});

$(document).click(function() {
	$('.options-popup').addClass('display-none').removeClass('popup-high popup-low');
});

$('body').on('click', '.options-popup', function(e) {
	e.stopPropagation();
})

$('body').on('click', '.option-delete', function(e) {
	var post_wrapper, data;

	post_wrapper = $(this).parents('.post-wrapper, post-fade');
	data = {post_id: post_wrapper.find('.post-id').html()};

	e.preventDefault();
	$(this).parent().addClass('display-none');
	post_wrapper.addClass('post-hidden');

	setTimeout (function() {
		post_wrapper.remove();
	}, 700);
	
	(function delete_post_db() {
		$.ajax({
			url: "/blog/delete_post",
			type: "POST",
			data: data,
		});
	}());

});