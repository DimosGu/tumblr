var follow_click_verify = true;

function follow(username) {
	$.ajax({
		url: '/following/follow',
		type: 'POST',
		data: {
			'username': username
		},

		success: function() {
			var $following, follow_count;

			$following = $('#li-following').find('span');
			follow_count = parseInt($following.html());
			follow_count += 1;

			$following.html(follow_count);
			follow_click_verify = true;
		}
	});
};

function unfollow(username) {
	$.ajax({
		url: '/following/unfollow',
		type: 'POST',
		data: {
			'username': username
		},

		success: function() {
			var $following, follow_count;

			$following = $('#li-following').find('span');
			follow_count = parseInt($following.html());
			follow_count -= 1;

			$following.html(follow_count);
			follow_click_verify = true;
		}
	});
};




$('body').on('click', '.follow', function (e) {
	var username = $(this).parent().attr('data-username');

	e.preventDefault();

	if (follow_click_verify) {
		follow_click_verify = false;
		follow(username);

		$(this).addClass('display-none');
		$(this).siblings('.unfollow').removeClass('display-none');

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
	}
});

$('body').on('click', '.unfollow', function (e) {
	var username = $(this).parent().attr('data-username');

	e.preventDefault();

	if (follow_click_verify) {
		follow_click_verify = false;
		unfollow(username);

		$(this).addClass('display-none');
		$(this).siblings('.follow').removeClass('display-none');

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
	}
});

