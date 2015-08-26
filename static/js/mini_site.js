var $mini_site_wrapper, $mini_site, $mini_posts_wrapper;

$mini_site_wrapper = $('#mini-site-wrapper');
$mini_site = $('#mini-site');

function get_site(username) {
	$.ajax({
		url: '/sites/mini_site',
		type: 'GET',
		data: {
			'clicked_user': username,
		},

		success: function(json) {
			setTimeout (function() {
				$mini_site.prepend(json.html);
			}, 200);

			setTimeout (function() {
				var $mini_posts_wrapper = $('#mini-posts-wrapper');
				$mini_posts_wrapper.prepend(json.post_html)
			}, 1000);
		},
	});
};

$('body').on('click', '.blog-link, .user-link', function (e) {
	var username = $(this).parents('.post-wrapper').attr('data-username');
	e.preventDefault();
	$('body').addClass('overflow-hidden2');
	$mini_site_wrapper.removeClass('display-none');
	get_site(username);

	setTimeout (function() {
		$mini_site.removeClass('site-no-width').addClass('site-width');
	}, 100);
});

$mini_site_wrapper.on('click', function (e) {
	var mini_site = document.getElementById('mini-site');
	var full_img = document.getElementById('full-screen-img');

	if (e.target === mini_site || $(e.target).parents('#mini-site').length) {
		return e.target;
	} else {	
		$('body').removeClass('overflow-hidden2');
		$mini_site.addClass('site-no-width').removeClass('site-width');
		$mini_site.empty();

		setTimeout (function() {
			$mini_site_wrapper.addClass('display-none');
		}, 200);
	}
});