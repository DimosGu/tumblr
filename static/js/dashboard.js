var get_post_verify, visible_posts;

visible_posts = 10;
get_post_verify = true;

function get_ten_posts(post_count) {
  $.ajax({
    url: "/dashboard/get_ten_posts",
    type: "GET",
    data: {
      'post_count': post_count
    },

    success: function(json) {
      var $posts_wrapper = $('#dashboard-posts-wrapper');

      $posts_wrapper.append(json.html);
      $('#loading-anim-container').remove();

      if (json.html.length) {
        setTimeout (function() {
          get_post_verify = true;
        }, 100);
      }
    }
  });
};