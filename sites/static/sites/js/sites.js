var get_post_veriy, visible_posts, site_username, $follow, $unfollow;

visible_posts = 10;
get_post_verify = true;
site_username = $('#link-wrapper').attr('data-username');

function get_ten_posts(post_count, site_user) {

	$.ajax({
		url: "/sites/get_ten_posts",
		type: "GET",
		data: {
			'post_count': post_count,
			'site_user': site_user,
		},

		success: function(json) {
			var $posts_wrapper = $('#posts-wrapper');

			$posts_wrapper.append(json.html);
			if (json.html.length) {
				get_post_verify = true;
			}
		},
	});
};

$(window).on('scroll', function() {
	if ($(window).scrollTop() + $(window).height() > $(document).height() / 1.25) {
		if (get_post_verify) {
			get_ten_posts(visible_posts, site_username);		
			get_post_verify = false;
			visible_posts += 10;
		}
	}
});

$follow = $('.follow');
$unfollow = $('.unfollow');

$follow.on('click', function() {
	$(this).addClass('display-none');
	$unfollow.removeClass('display-none');
});

$unfollow.on('click', function() {
	$(this).addClass('display-none');
	$follow.removeClass('display-none');
});