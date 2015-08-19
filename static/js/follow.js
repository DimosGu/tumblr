function follow_blog(username) {
	$.ajax({
		url: '/blog/follow_blog',
		type: 'POST',
		data: {
			'username': username
		}
	});
};

function unfollow_blog(username) {
	$.ajax({
		url: '/blog/unfollow_blog',
		type: 'POST',
		data: {
			'username': username
		}
	});
};

$('.follow').on('click', function (e) {
	var username = $(this).parents().siblings('.user-link').html();
	e.preventDefault();
	$(this).addClass('display-none');
	$(this).siblings('.unfollow').removeClass('display-none');
	follow_blog(username);
});

$('.unfollow').on('click', function(e) {
	var username = $(this).parents().siblings('.user-link').html();
	e.preventDefault();
	$(this).addClass('display-none');
	$(this).siblings('.follow').removeClass('display-none');
	unfollow_blog(username);
});