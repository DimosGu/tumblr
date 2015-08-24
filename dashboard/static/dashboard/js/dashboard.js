var get_post_verify, visible_posts;

visible_posts = 10;
get_post_verify = true;

$(document).ready(function() {
	var post_img = document.querySelectorAll('.post-img');

	setTimeout (function() {
		if ($(document).height() === $(window).height()) {
			get_ten_posts(visible_posts);		
			get_post_verify = false;
			visible_posts += 10;
		}
	}, 1000)
})

function get_ten_posts(post_count) {
	$.ajax({
		url: "/dashboard/get_ten_posts",
		type: "GET",
		data: {
			'post_count': post_count
		},

		success: function(json) {
			var $posts_wrapper = $('#posts-wrapper');

			$posts_wrapper.append(json.html);
			if (json.html.length) {
				get_post_verify = true;
			}
		}
	});
};

$(window).on('scroll', function() {
	if ($(window).scrollTop() + $(window).height() > $(document).height() / 1.25) {
		if (get_post_verify) {
			get_ten_posts(visible_posts);		
			get_post_verify = false;
			visible_posts += 10;
		}
	}
});