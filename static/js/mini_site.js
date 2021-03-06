var $mini_site_wrapper, $mini_site, mini_visible_posts, mini_get_post_verify;

$mini_site_wrapper = $('#mini-site-wrapper');
$mini_site = $('#mini-site');

function get_blog(username) {
	$.ajax({
		url: '/sites/mini_site',
		type: 'GET',
		data: {
			'clicked_user': username,
		},

		success: function(json) {
			var mini_site = document.getElementById('mini-site');

			setTimeout (function() {
				$mini_site.prepend(json.html);
			}, 200);

			setTimeout (function() {
				$('#mini-posts-wrapper').prepend(json.post_html);
				var scrollbar_size = mini_site.offsetWidth - mini_site.clientWidth;

				$('#mini-header-overlay').css({
					'right': scrollbar_size,
					'width': mini_site.clientWidth
				});
			}, 500);
		},
	});
};

$('body').on('click', '.blog-link, .user-link', function(e) {
	var username = $(this).parents('.post-wrapper').attr('data-username');
	e.preventDefault();
	$('body').addClass('overflow-hidden2');
	$mini_site_wrapper.removeClass('display-none');
	get_blog(username);

	setTimeout (function() {
		$mini_site.removeClass('site-no-width').addClass('site-width');
	}, 100);
});

mini_visible_posts = 10;
mini_get_post_verify = true;

function mini_get_ten_posts(username, visible_posts) {
	$.ajax({
		url: '/sites/get_ten_posts',
		type: 'GET',
		data: {
			'site_user': username,
			'post_count': visible_posts,
			'mini': 'mini',
		},

		success: function(json) {
			$('#mini-posts-wrapper').append(json.html);
			$('#loading-anim-container').remove();

			if (json.html.length) {
				setTimeout (function() {
					mini_get_post_verify = true;
				}, 100);
			}
		}
	});
};

$('#mini-site').on('scroll', function() {
	if ($(this).scrollTop() + $(this).height() > $(this)[0].scrollHeight / 1.25) {
		var username = $('#mini-link-wrapper').attr('data-username');

		if (mini_get_post_verify) {
			var mini = true;
			append_loading_anim(mini);
			mini_get_ten_posts(username, mini_visible_posts);
			mini_get_post_verify = false;
			mini_visible_posts += 10;
		}
	}
});

$mini_site_wrapper.on('click', function(e) {
	var mini_site = document.getElementById('mini-site');
	var full_img = document.getElementById('full-screen-img');

	if (e.target === mini_site || $(e.target).parents('#mini-site').length) {
		return e.target;
	} else {
		mini_get_post_verify = false;
		$('body').removeClass('overflow-hidden2');
		$mini_site.addClass('site-no-width').removeClass('site-width');
		$mini_site.empty();

		setTimeout (function() {
			$mini_site_wrapper.addClass('display-none');
		}, 200);

		setTimeout (function() {
			mini_visible_posts = 10;
			mini_get_post_verify = true;
		}, 1000);
	}
});

$('body').on('mouseenter', '#mini-site-link', function() {
	$(this).children('span').removeClass('invisible').addClass('visible');
});

$('body').on('mouseleave', '#mini-site-link', function() {
	$(this).children('span').removeClass('visible').addClass('invisible');
});