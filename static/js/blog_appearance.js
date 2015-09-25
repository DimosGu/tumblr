var edit_verify, save_verify, $save, $mini_header, $mini_header_original_image,
    $avatar_img, $avatar_original_img, $header_img_input, $avatar_img_input,
    $blog_title, $title_span, $original_title, $edit_appearance, $edit_appearance_text,
    $mini_site_link, $edit_options_wrapper, $edit_options_cover;

edit_verify = true;
save_verify = false;
$save = $('#save');

animation_html = '<div id="waiting-anim-container"><div class="waiting-rect"></div>' +
  '<div class="waiting-rect"></div><div class="waiting-rect"></div></div>'

$blog_appearance_wrapper = $('#blog-appearance-wrapper');

$mini_header = $('#mini-header');
$mini_header_original_image = $mini_header.attr('style');
$avatar_img = $('#mini-blog-img').children('img');
$avatar_original_img = $avatar_img.attr('src');

$header_img_input = $('#header-img-input');
$avatar_img_input = $('#avatar-img-input');

$blog_title = $('#mini-blog-info').children('h1');
$title_span = $blog_title.children('span');
$original_title = $title_span.html();

$edit_appearance = $('#edit-appearance');
$edit_appearance_html = $edit_appearance.html();
$edit_appearance_text = $('#edit-appearance-text');

$mini_site_link = $('#mini-site-link');
$edit_options_wrapper = $('#edit-options-wrapper');
$edit_options_cover = $('#edit-options-cover');

$edit_appearance.on('click', function() {
  if (edit_verify) {
    $(this).addClass('display-none');
    $mini_site_link.addClass('display-none');
    $edit_options_cover.removeClass('display-none');
    $edit_options_wrapper.removeClass('display-none');
    $title_span.attr('contentEditable', 'true');
    $title_span.addClass('title-border');
  }
});

$('#cancel').on('click', function() {
  $edit_options_wrapper.addClass('display-none');
  $edit_options_cover.addClass('display-none');
  $edit_appearance.removeClass('display-none');
  $mini_site_link.removeClass('display-none');

  $mini_header.attr('style', $mini_header_original_image);
  $header_img_input.val('');
  $avatar_img.attr('src', $avatar_original_img);
  $avatar_img_input.val('');

  $title_span.removeAttr('contentEditable');
  $title_span.removeClass('title-border');
  $title_span.html($original_title);
  $title_span.removeAttr('data-placeholder');

  save_verify = false;
  $save.addClass('save-font-color');
});

$blog_pk = $('#wrapper').attr('data-blog-pk');

function edit_blog(blog_pk) {
  var $blog_data;
  $blog_data = new FormData($('#blog-change-form')[0]);

  $blog_data.append('blog_pk', blog_pk);

  if ($original_title !== $title_span.html() && $title_span.html() !== '') {
    $blog_data.append('blog_title', $title_span.html());
  }

  data = $blog_data;

  $.ajax({
    url: "/settings/edit_blog",
    type: "POST",
    data: data,
    processData: false,
    contentType: false,

    success: function(json) {
      edit_verify = true;

      $('#waiting-anim-container').remove();
      $edit_appearance.html($edit_appearance_html);

      $header_img_input.val('');
      $avatar_img_input.val('');

      $mini_header_original_image = $mini_header.attr('style');
      $avatar_original_img = $avatar_img.attr('src');
      $original_title = $title_span.html();
    }
  })
}

$save.on('click', function() {
  if (save_verify) {
    save_verify = false;
    edit_verify = false;

    $save.addClass('save-font-color');

    $title_span.removeAttr('contentEditable');
    $title_span.removeClass('title-border');
    $title_span.removeAttr('data-placeholder');

    $edit_options_wrapper.addClass('display-none');
    $edit_options_cover.addClass('display-none');

    $edit_appearance.html('');
    $edit_appearance.removeClass('display-none');

    $mini_site_link.removeClass('display-none');

    if ($title_span.html() === '') {
      $title_span.html($original_title);
    }

    edit_blog($blog_pk);
    $blog_appearance_wrapper.prepend(animation_html);
  }
});

$('#edit-header-img').on('click', function() {
  $header_img_input.click()
});

$header_img_input.change(function() {

  save_verify = true;
  $save.removeClass('save-font-color');

  if (this.files && this.files[0]) {
    var reader = new FileReader();

    reader.onload = function(e) {
      $mini_header.attr('style', "background-image: url(" + e.target.result + ")");
    }
  }

  reader.readAsDataURL(this.files[0]);
});

$('#edit-avatar').on('click', function() {
  $avatar_img_input.click();
});

$avatar_img_input.change(function() {

  save_verify = true;
  $save.removeClass('save-font-color');

  if (this.files && this.files[0]) {
    var reader = new FileReader();

    reader.onload = function(e) {
      $avatar_img.attr('src', e.target.result);
    }
  }

  reader.readAsDataURL(this.files[0]);
});

$title_span.on('focus', function() {
  $title_span.removeClass('title-border');
  $blog_title.addClass('h1-focus');
});

$title_span.on('blur', function() {
  $title_span.addClass('title-border');
  $blog_title.removeClass('h1-focus')
});

$title_span.on('keyup keydown', function() {

  if (save_verify == false) {
    save_verify = true;
    $save.removeClass('save-font-color');
  }

  if ($title_span.html() === '') {
    $(this).attr('data-placeholder', 'Title');
  }

  setTimeout (function() {
    if (typeof $title_span.attr('data-placeholder') !== 'undefined' && $title_span.html() !== '') {
      $title_span.removeAttr('data-placeholder');
    }
  }, 1);
});