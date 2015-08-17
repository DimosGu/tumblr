var $posts, visible_posts, get_post_verify, post_edit_id;

$posts = $('.post-wrapper');
visible_posts = 10;
get_post_verify = true;

function blog_onload() {
	var blog_post_img = document.querySelectorAll('.blog-post-img');
	
	for (var i = 0; i < blog_post_img.length; i++) {
		if (blog_post_img[i].width <= 522) {
			blog_post_img[i].style.marginLeft = '18px';
		}
	}

	//actual tumblr site bug fix. loads more posts if there is no scroll bar.
	setTimeout (function() {
		if ($(document).height() === $(window).height()) {
			get_ten_posts(visible_posts);		
			get_post_verify = false;
			visible_posts += 10;
		}
	}, 1000)
}

function get_ten_posts(post_count) {
	$.ajax({
		url: "/blog/get_more_posts",
		type: "GET",
		data: {
			'post_count': post_count
		},

		success: function(json) {
			var $post_wrapper = $('#blog-posts-wrapper');

			$post_wrapper.append(json.html);
			if (json.html.length) {
				get_post_verify = true;
			}
		},
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

$('body').on('click', '.blog-footer-options', function() {
	var $footer_options = $(this).find('.options-popup');

	if ($footer_options.hasClass('display-none')) {

		setTimeout (function() {
			$footer_options.removeClass('display-none');		

			if($footer_options.offset().top - $(window).scrollTop() >= 
				window.innerHeight - $footer_options.height() - 22) {
				$footer_options.addClass('popup-high');
			} else {
				$footer_options.addClass('popup-low');
			}
		}, 1);
	}
});

$(document).click(function() {
	$('.options-popup').addClass('display-none').removeClass('popup-high popup-low');
});

$('body').on('click', '.options-popup', function (e) {
	e.stopPropagation();
})

function prepare_header_text_form(target) {
	var $post_wrapper, $blog_title, $blog_text, $blog_tags;

	post_types[0].click();
	
	$post_wrapper = target.parents('.post-wrapper');

	post_options.className = "post-fade visible";
	post_submit_button[0].className = "submit-button button-color";
	post_submit_button[0].innerHTML = "Save";

	$blog_title = $post_wrapper.find('.blog-post-title').html();

	if ($blog_title === undefined) {
		title_field[0].value = "";
	} else {
		title_field[0].value = $blog_title;
	}

	$blog_text = $post_wrapper.find('.blog-post-text').html();

	if ($blog_text === undefined) {
		text_field[0].value = "";
	} else {
		text_field[0].value = $blog_text;
	}

	$blog_tags = $post_wrapper.find('.blog-post-tags').html();

	if ($blog_tags === undefined) {
		tags_field[0].value = "";
	} else {
		tags_field[0].value = $blog_tags;
	}
}

function prepare_header_photo_form(target) {
	var $img_preview, $post_wrapper, $post_photo, $blog_text, $blog_tags;
	
	post_types[1].click();

	$img_preview = $("#img-preview");
	$post_wrapper = target.parents('.post-wrapper');
	$post_photo = $post_wrapper.find('.blog-post-img');

	$('#image-option').addClass("display-none");
	$photo_content.removeClass("display-none");
  $img_preview.removeClass("display-none");
	$img_preview.attr('src', $post_photo.attr('src'));
	post_options.className = "post-fade visible";
	post_submit_button[1].className = "submit-button button-color";
	post_submit_button[1].innerHTML = "Save";

	file_field[0].value = "";

	$blog_text = $post_wrapper.find('.blog-post-text').html()

	if ($blog_text === undefined) {
		text_field[1].value = "";
	} else {
		text_field[1].value = $blog_text;
	}

	$blog_tags = $post_wrapper.find('.blog-post-tags').html();

	if ($blog_tags === undefined) {
		tags_field[1].value = "";
	} else {
		tags_field[1].value = $blog_tags;
	}
}

post_edit_id = null;

$('body').on('click', '.option-edit', function (e) {
	var $post_wrapper, $post_photo, post_id;

	e.preventDefault();
	$(this).parent().addClass('display-none');

	$post_wrapper = $(this).parents('.post-wrapper');
	$post_photo = $post_wrapper.find('.blog-post-img');

	//This sets the id of the post instance to be carried to the ajax request
	post_edit_id = $post_wrapper.find('.post-id').html();

	if ($post_photo.length) {
		prepare_header_photo_form($(this));
	} else {
		prepare_header_text_form($(this));
	}
});


$('body').on('click', '.option-delete', function (e) {
	var $post_wrapper, $post_id;

	e.preventDefault();

	$post_wrapper = $(this).parents('.post-wrapper');
	$post_id = $post_wrapper.find('.post-id').html()

	$(this).parent().addClass('display-none');
	$post_wrapper.addClass('invisible');

	setTimeout (function() {
		$post_wrapper.remove();
		visible_posts -= 1;

		(function delete_post_db() {
			$.ajax({
				url: "/blog/delete_post",
				type: "POST",
				data: {
					'post_id': $post_id
				},
			});
		}());
	}, 700);
});