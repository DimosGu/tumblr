function follow(username) {
	$.ajax({
		url: '/following/follow',
		type: 'POST',
		data: {
			'username': username
		}
	});
};

function unfollow(username) {
	$.ajax({
		url: '/following/unfollow',
		type: 'POST',
		data: {
			'username': username
		}
	});
};

$('body').on('click', '.follow', function (e) {
	e.preventDefault();

	var username = $(this).parent().attr('data-username');
	follow(username);

	if ((typeof explore_body !== 'undefined' && explore_body) ||
		(typeof likes_body !== 'undefined' && likes_body)) {
		var $post_wrapper = $('.post-wrapper');

		for (var i = 0; i < $post_wrapper.length; i++) {
			var same_user = $post_wrapper.eq(i).find('.user-link').html();

			if (explore_body && username === same_user) {
				$post_wrapper.eq(i).find('.follow').addClass('display-none');
				$post_wrapper.eq(i).find('.unfollow').removeClass('display-none');
			} else if (likes_body && username == same_user) {
				$post_wrapper.eq(i).find('.follow').remove()
			}
		}
	}
});

$('body').on('click', '.unfollow', function (e) {
	e.preventDefault();

	var username = $(this).parent().attr('data-username');
	unfollow(username);

	if (typeof explore_body !== 'undefined' && explore_body) {
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

