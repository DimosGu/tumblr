var visible_posts, get_post_verify, $post_wrapper, $post_content;

$post_wrapper = $('.post-wrapper');
$post_content = $('#post-content');

$(window).load(function() {
	setTimeout (function() {
		$post_content.masonry({
			itemSelector: '.post-wrapper',
			isFitWidth: true,
			transitionDuration: 0,
			gutter: 20
		});
	}, 1);

	setTimeout (function() {
		$('#wrapper').removeClass('invisible');
		$post_wrapper.removeClass('invisible');
		get_ten_posts(visible_posts);		
		visible_posts += 10;
		get_post_verify = false;
	}, 1000);
});

visible_posts = 10;
get_post_verify = true;

function get_ten_posts(post_count) {
	$.ajax({
		url: "/explore/get_ten_posts",
		type: "GET",
		data: {
			'post_count': post_count
		},

		success: function(json) {

			$post_content.append(json.html);
			$post_content.masonry('reloadItems');

			setTimeout (function() {
				$post_content.masonry('layout');
			}, 300);

			setTimeout (function() {
				var $post_wrapper = $('.post-wrapper');	
				$post_wrapper.removeClass('invisible');
			}, 500);

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