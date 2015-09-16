var visible_posts, get_post_verify, $post_wrapper, $post_content;

$post_wrapper = $('.post-wrapper');
$explore_post_wrapper = $('#explore-posts-wrapper');
visible_posts = 10;
get_post_verify = true;

$(window).load(function() {

  setTimeout (function() {
    $explore_post_wrapper.masonry({
      itemSelector: '.post-wrapper',
      isFitWidth: true,
      transitionDuration: 0,
      gutter: 20
    });

    $('#wrapper').removeClass('invisible');
    $post_wrapper.removeClass('invisible');
  }, 1);
});

function get_ten_posts(post_count) {
  var $body_attr, url;

  $body_attr = $('body').attr('data');

  if ($body_attr) {
    url = "/search/get_ten_posts/" + $body_attr;
  } else {
    url = "/explore/get_ten_posts";
  }

  $.ajax({
    url: url,
    type: "GET",
    data: {
      'post_count': post_count
    },

    success: function(json) {
      if (json.html && json.html != "NoResults") {
        $explore_post_wrapper.append(json.html);
        $explore_post_wrapper.masonry('reloadItems');

        setTimeout (function() {
          $explore_post_wrapper.masonry('layout');
        }, 300);

        setTimeout (function() {
          var $post_wrapper = $('.post-wrapper');
          $post_wrapper.removeClass('invisible');
          get_post_verify = true;
        }, 500);

      } else if (json.html === undefined) {
        return json.html;
      } else {
        $explore_post_wrapper.after("<div id='end-results'><p>That's about it for <span>" + json.result + "</span>. Try another search?</p></div>")
      }
    }
  });
};