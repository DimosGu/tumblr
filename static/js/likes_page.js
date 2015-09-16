var get_post_verify, visible_posts;

visible_posts = 10;
get_post_verify = true;

$(window).load(function() {

  setTimeout (function() {
    if ($(document).height() === $(window).height()) {
      get_ten_posts(visible_posts);
      get_post_verify = false;
      visible_posts += 10;
    }
  }, 1000)
})

function get_ten_posts(post_count) {
  $.ajax({
    url: "/likes/ten_more_posts",
    type: "GET",
    data: {
      'post_count': post_count
    },

    success: function(json) {
      var $posts_wrapper = $('#likes-posts-wrapper');

      $posts_wrapper.append(json.html);
      if (json.html.length) {
        get_post_verify = true;
      }
    }
  });
};