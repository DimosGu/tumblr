function follow(username) {
	$.ajax({
		url: '/blog/follow',
		type: 'POST',
		data: {
			'username': username
		}
	});
};

function unfollow(username) {
	$.ajax({
		url: '/blog/unfollow',
		type: 'POST',
		data: {
			'username': username
		}
	});
};

$('body').on('click', '.follow', function (e) {
	var username = $(this).parent().attr('data-username');
	follow(username);

	if (explore_body) {
		var $post_wrapper = $('.post-wrapper');

		for (var i = 0; i < $post_wrapper.length; i++) {
			var same_user = $post_wrapper.eq(i).find('.user-link').html();

			if (username === same_user) {
				$post_wrapper.eq(i).find('.follow').addClass('display-none');
				$post_wrapper.eq(i).find('.unfollow').removeClass('display-none');
			}
		}
	}
});

$('body').on('click', '.unfollow', function (e) {
	var username = $(this).parent().attr('data-username');
	unfollow(username);

	if (explore_body) {
		var $post_wrapper = $('.post-wrapper');

		for (var i = 0; i < $post_wrapper.length; i++) {
			var same_user = $post_wrapper.eq(i).find('.user-link').html();
			if (username === same_user) {
				$post_wrapper.eq(i).find('.unfollow').addClass('display-none');
				$post_wrapper.eq(i).find('.follow').removeClass('display-none');
			}
		}
	}
});
