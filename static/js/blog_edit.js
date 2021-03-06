var visible_posts, get_post_verify, post_edit_id;

visible_posts = 10;
get_post_verify = true;

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
			$('#loading-anim-container').remove();

			if (json.html.length) {
				setTimeout (function() {
					get_post_verify = true;
				}, 100);
			}
		}
	});
};

$('body').on('click', '.post-edit', function() {
	var $footer_options = $(this).siblings('.options-popup');

	if ($footer_options.hasClass('display-none')) {

		setTimeout (function() {
			$footer_options.removeClass('display-none');

			if($footer_options.offset().top - $(window).scrollTop() >=
				window.innerHeight - $footer_options.height() - 10) {
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

$('body').on('click', '.options-popup', function(e) {
	e.stopPropagation();
})

function prepare_header_text_form(target) {
	var $post_wrapper, $blog_title, $post_text, $post_tags, tags_array, tags_join;

	post_types[0].click();

	$post_wrapper = target.parents('.post-wrapper');

	post_options.className = "post-fade visible";
	post_submit_button[0].className = "submit-button button-color";
	post_submit_button[0].innerHTML = "Save";

	$blog_title = $post_wrapper.find('.post-title').html();

	if ($blog_title === undefined) {
		title_field[0].value = "";
	} else {
		title_field[0].value = $blog_title;
	}

	$post_text = $post_wrapper.find('.post-text').html();

	if ($post_text === undefined) {
		text_field[0].value = "";
	} else {
		text_field[0].value = $post_text;
	}

	$post_tags = $post_wrapper.find('.post-tags').children();

	if ($post_tags.length) {

		tags_array = [];
		tags_array.push($post_tags.eq(0).text())

		for (var i = 1; i < $post_tags.length; i++) {
			tags_array.push('' + $post_tags.eq(i).text());
		}

		tags_join = tags_array.join(' ');
	}

	if ($post_tags.length === 0) {
		tags_field[0].value = "";
	} else {
		tags_field[0].value = tags_join;
	}

	//Adjusts field's height after inserting text
	check_title_field(title_field[0]);
	check_text_field(text_field[0]);
	check_tag_field(tags_field[0]);
}

function prepare_header_photo_form(target) {
	var $img_preview, $post_wrapper, $post_photo, $post_text, $post_tags,
			tags_array, tags_join;

	post_types[1].click();

	$img_preview = $("#img-preview");
	$post_wrapper = target.parents('.post-wrapper');
	$post_photo = $post_wrapper.find('.post-img');

	$('#image-option').addClass("display-none");
	$photo_content.removeClass("display-none");
  $img_preview.removeClass("display-none");
	$img_preview.attr('src', $post_photo.attr('src'));
	post_options.className = "post-fade visible";
	post_submit_button[1].className = "submit-button button-color";
	post_submit_button[1].innerHTML = "Save";

	file_field[0].value = "";

	$post_text = $post_wrapper.find('.post-text').html()

	if ($post_text === undefined) {
		text_field[1].value = "";
	} else {
		text_field[1].value = $post_text;
	}

	$post_tags = $post_wrapper.find('.post-tags').children();

	if ($post_tags.length) {

		tags_array = [];
		tags_array.push($post_tags.eq(0).text())

		for (var i = 1; i < $post_tags.length; i++) {
			tags_array.push('' + $post_tags.eq(i).text());
		}

		tags_join = tags_array.join(' ');
	}

	if ($post_tags.length === 0) {
		tags_field[1].value = "";
	} else {
		tags_field[1].value = tags_join;
	}

	//Adjusts field's height after inserting text
	check_text_field(text_field[1]);
	check_tag_field(tags_field[1]);
}

post_edit_id = null;

$('body').on('click', '.option-edit', function(e) {
	var $post_wrapper, $post_photo;

	e.preventDefault();
	$(this).parent().addClass('display-none');

	$post_wrapper = $(this).parents('.post-wrapper');
	$post_photo = $post_wrapper.find('.post-img');

	//This sets the id of the post instance to be used in post.js
	post_edit_id = $post_wrapper.attr('data-id');

	if ($post_photo.length) {
		prepare_header_photo_form($(this));
	} else {
		prepare_header_text_form($(this));
	}
});


$('body').on('click', '.option-delete', function(e) {
	var $post_wrapper, $post_id;

	e.preventDefault();

	$post_wrapper = $(this).parents('.post-wrapper');
	$post_id = $post_wrapper.attr('data-id');

	$(this).parent().addClass('display-none');
	$post_wrapper.addClass('invisible');

	setTimeout (function() {
		$post_wrapper.remove();
		visible_posts -= 1;

		$.ajax({
			url: "/blog/delete_post",
			type: "POST",
			data: {
				'post_id': $post_id
			},
		});
	}, 700);
});