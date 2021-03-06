var get_post_veriy, visible_posts, site_username, $follow, $unfollow;

visible_posts = 10;
get_post_verify = true;
site_username = $('#link-wrapper').attr('data-username');

$(window).load(function() {
	$('#wrapper').removeClass('display-none');
});

function get_ten_posts(post_count, site_user) {

	$.ajax({
		url: "/sites/get_ten_posts",
		type: "GET",
		data: {
			'post_count': post_count,
			'site_user': site_user,
		},

		success: function(json) {
			var $posts_wrapper = $('#sites-posts-wrapper');

			$posts_wrapper.append(json.html);
			$('#loading-anim-container').remove();

			if (json.html.length) {
				setTimeout (function() {
					get_post_verify = true;
				}, 100);
			}
		},
	});
};