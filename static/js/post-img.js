var $img_zoom = $('#full-screen-img');

$('body').on('click', '.blog-click-img', function (e) {
	e.preventDefault();
	var $img_url = $(this).attr('href');
	$('body').addClass('overflow-hidden');
	$img_zoom.children('img').attr('src', $img_url);
	$img_zoom.removeClass('display-none').addClass('img-overlay')
});

$img_zoom.on('click', function(e) {
	$('body').removeClass('overflow-hidden');
	$img_zoom.removeClass('img-overlay').addClass('display-none');
})