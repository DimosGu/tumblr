var get_post_verify, visible_posts;

visible_posts = 10;
get_post_verify = true;

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