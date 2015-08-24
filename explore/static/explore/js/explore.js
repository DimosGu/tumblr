var visible_posts, get_post_verify, $post_wrapper, $post_content;

$post_wrapper = $('.post-wrapper');
$post_content = $('#post-content');

$(document).ready(function() {

	setTimeout (function() {
		$post_content.masonry({
			itemSelector: '.post-wrapper',
			isFitWidth: true,
			transitionDuration: 0,
			gutter: 20
		});
		$('#wrapper').removeClass('invisible');
		$post_wrapper.removeClass('invisible');
	}, 1);
});

visible_posts = 10;
get_post_verify = true;

function explore_onload() {
	setTimeout (function() {
		get_ten_posts(visible_posts);		
		get_post_verify = false;
		visible_posts += 10;
	}, 1000)
}

function get_ten_posts(post_count) {
	$.ajax({
		url: "/explore/get_ten_posts",
		type: "GET",
		data: {
			'post_count': post_count
		},

		success: function(json) {

			$post_content.append(json.html);
			$post_content.masonry( 'reloadItems' );

			setTimeout (function() {
				$post_content.masonry( 'layout' );
			}, 100);

			setTimeout (function() {
				var $post_wrapper = $('.post-wrapper');	
				$post_wrapper.removeClass('invisible');
			}, 200);

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

$('body').on('click', '.follow', function () {
	var clicked_user = $(this).parents('.post-wrapper').find('.user-link').html();
	var $post_wrapper = $('.post-wrapper');

	for (var i = 0; i < $post_wrapper.length; i++) {
		var same_user = $post_wrapper.eq(i).find('.user-link').html();
		if (clicked_user === same_user) {
			$post_wrapper.eq(i).find('.follow').addClass('display-none');
			$post_wrapper.eq(i).find('.unfollow').removeClass('display-none');
		}
	}
});

$('body').on('click', '.unfollow', function () {
	var clicked_user = $(this).parents('.post-wrapper').find('.user-link').html();
	var $post_wrapper = $('.post-wrapper');

	for (var i = 0; i < $post_wrapper.length; i++) {
		var same_user = $post_wrapper.eq(i).find('.user-link').html();
		if (clicked_user === same_user) {
			$post_wrapper.eq(i).find('.unfollow').addClass('display-none');
			$post_wrapper.eq(i).find('.follow').removeClass('display-none');
		}
	}
});