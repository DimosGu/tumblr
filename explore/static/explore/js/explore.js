var $post_container = $('#post-content');
var $wrapper = $('#wrapper');
var $post_wrapper = $('.post-wrapper');

$(window).load( function() {

	for (var i = 0; i < $post_wrapper.length; i++) {
		var $following = $post_wrapper.eq(i).children('.following').html()
		if ($following === 'true') {
			$post_wrapper.eq(i).find('.follow').addClass('display-none');
			$post_wrapper.eq(i).find('.unfollow').removeClass('display-none');
		}
	}

	setTimeout (function() {
		$('#post-content').masonry({
			itemSelector: '.post-wrapper',
			isFitWidth: true,
			transitionDuration: 0
		});
		$wrapper.removeClass('invisible');
	}, 1);
});

$('.follow').on('click', function () {
	var clicked_user = $(this).parents().find('.user-link').html();

	for (var i = 0; i < $post_wrapper.length; i++) {
		var same_user = $post_wrapper.eq(i).find('.user-link').html();
		if (clicked_user === same_user) {
			$post_wrapper.eq(i).find('.follow').addClass('display-none');
			$post_wrapper.eq(i).find('.unfollow').removeClass('display-none');
		}
	}
});

$('.unfollow').on('click', function () {
	var clicked_user = $(this).parents().find('.user-link').html();

	for (var i = 0; i < $post_wrapper.length; i++) {
		var same_user = $post_wrapper.eq(i).find('.user-link').html();
		if (clicked_user === same_user) {
			$post_wrapper.eq(i).find('.unfollow').addClass('display-none');
			$post_wrapper.eq(i).find('.follow').removeClass('display-none');
		}
	}
});