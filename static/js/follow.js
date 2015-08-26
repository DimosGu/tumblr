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
	console.log(username);
	follow(username);
});

$('body').on('click', '.unfollow', function (e) {
	var username = $(this).parent().attr('data-username');
	console.log(username);
	unfollow(username);
});