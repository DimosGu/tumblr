var $mini_site_wrapper, $mini_site, mini_visible_posts, mini_get_post_verify;

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
				$('#mini-posts-wrapper').prepend(json.post_html);
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

			if (json.html.length) {
				mini_get_post_verify = true;
			}
		}
	});
};
$('#mini-site').on('scroll', function() {
	console.log(mini_visible_posts);
	if ($(this).scrollTop() + $(this).height() > $(this)[0].scrollHeight / 1.25) {
		var username = $('#mini-link-wrapper').attr('data-username');

		if (mini_get_post_verify) {
			mini_get_ten_posts(username, mini_visible_posts);		
			mini_get_post_verify = false;
			mini_visible_posts += 10;
		}
	}
});


$mini_site_wrapper.on('click', function (e) {
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

/*These functions are bound to the body because the elements 
don't exist when the dom is initially loaded.*/

$('body').on('click', '#mini-follow', function() {
	$(this).addClass('display-none');
	$('#mini-unfollow').removeClass('display-none');
});

$('body').on('click', '#mini-unfollow', function() {
	$(this).addClass('display-none');
	$('#mini-follow').removeClass('display-none');
});

$('body').on('mouseenter', '#mini-site-link', function() {
	$(this).children('span').removeClass('invisible').addClass('visible');
});

$('body').on('mouseleave', '#mini-site-link', function() {
	$(this).children('span').removeClass('visible').addClass('invisible');
});