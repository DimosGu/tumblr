var $img_zoom = $('#full-screen-img');

$(document).on('click', '.post-click-img', function (e) {
	e.preventDefault();
	var $img_url = $(this).attr('href');
	$('body').addClass('overflow-hidden');
	$img_zoom.children('img').attr('src', $img_url);
	$img_zoom.removeClass('display-none');
});

$img_zoom.on('click', function() {
	$('body').removeClass('overflow-hidden');
	$img_zoom.addClass('display-none');
	$img_zoom.children('img').attr('src', '');
});