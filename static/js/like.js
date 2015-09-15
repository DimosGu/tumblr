function like(post_pk) {
  $.ajax({
    url: '/blog/like',
    type: 'POST',
    data: {
      'post_pk': post_pk
    }
  });
};

function unlike(post_pk) {
  $.ajax({
    url: '/blog/unlike',
    type: 'POST',
    data: {
      'post_pk': post_pk
    }
  });
};

$(document).on('click', '.like', function (e) {
  var post_id = $(this).parents('.post-wrapper').attr('data-id');
  unlike(post_id);
  $(this).addClass('display-none');
  $(this).siblings('.no-like').removeClass('display-none');

  if ($(this).parents('#mini-site')) {
    var $same_post = $('#wrapper').find('.post-wrapper' + "[data-id='" + post_id + "']");
    $same_post.find('.like').addClass('display-none');
    $same_post.find('.no-like').removeClass('display-none');
  }
});

$(document).on('click', '.no-like', function (e) {
  var post_id = $(this).parents('.post-wrapper').attr('data-id');
  like(post_id);
  $(this).addClass('display-none');
  $(this).siblings('.like').removeClass('display-none');

  if ($(this).parents('#mini-site')) {
    var $same_post = $('#wrapper').find('.post-wrapper' + "[data-id='" + post_id + "']");
    $same_post.find('.no-like').addClass('display-none');
    $same_post.find('.like').removeClass('display-none');
  }
});