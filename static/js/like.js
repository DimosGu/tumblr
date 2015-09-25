var like_click_verify = true;

function like(post_pk) {
  $.ajax({
    url: '/likes/like',
    type: 'POST',
    data: {
      'post_pk': post_pk
    },

    success: function() {
      var $likes, like_count, like_increase;

      $likes = $('#li-likes').find('span');
      like_count = parseInt($likes.html());
      like_count += 1;

      $likes.html(like_count);
      like_click_verify = true;
    }
  });
};

function unlike(post_pk) {
  $.ajax({
    url: '/likes/unlike',
    type: 'POST',
    data: {
      'post_pk': post_pk
    },

    success: function() {
      var $likes, like_count, like_increase;

      $likes = $('#li-likes').find('span');
      like_count = parseInt($likes.html());
      like_count -= 1;

      $likes.html(like_count);
      like_click_verify = true;
    }
  });
};

$(document).on('click', '.like', function(e) {
  var post_id = $(this).parents('.post-wrapper').attr('data-id');

  if (like_click_verify) {
    like_click_verify = false;
    unlike(post_id);

    $(this).addClass('display-none');
    $(this).siblings('.no-like').removeClass('display-none');

    if ($(this).parents('#mini-site')) {
      var $same_post = $('#wrapper').find('.post-wrapper' + "[data-id='" + post_id + "']");
      $same_post.find('.like').addClass('display-none');
      $same_post.find('.no-like').removeClass('display-none');
    }
  }
});

$(document).on('click', '.no-like', function(e) {
  var post_id = $(this).parents('.post-wrapper').attr('data-id');

  if (like_click_verify) {
    like_click_verify = false;
    like(post_id);

    $(this).addClass('display-none');
    $(this).siblings('.like').removeClass('display-none');

    if ($(this).parents('#mini-site')) {
      var $same_post = $('#wrapper').find('.post-wrapper' + "[data-id='" + post_id + "']");
      $same_post.find('.no-like').addClass('display-none');
      $same_post.find('.like').removeClass('display-none');
    }
  }

});