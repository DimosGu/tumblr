var visible_posts, get_post_verify, $post_wrapper, $post_content;

$post_wrapper = $('.post-wrapper');
$post_content = $('#post-content');
visible_posts = 10;
get_post_verify = true;

$(window).load(function() {
  setTimeout (function() {

    $post_content.masonry({
      itemSelector: '.post-wrapper',
      isFitWidth: true,
      transitionDuration: 0,
      gutter: 20
    });

    $('#wrapper').removeClass('invisible');
    $post_wrapper.removeClass('invisible');
  }, 1);

  setTimeout (function() {
    if ($(document).height() === $(window).height()) {
      get_post_verify = false;
      visible_posts += 10;
      get_ten_posts(visible_posts);
    }
  }, 1000)
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
      if (json.html.length >= 1 && json.html != "NoResults") {
        $post_content.append(json.html);
        $post_content.masonry('reloadItems');

        setTimeout (function() {
          $post_content.masonry('layout');
        }, 300);

        setTimeout (function() {
          var $post_wrapper = $('.post-wrapper');
          $post_wrapper.removeClass('invisible');
          get_post_verify = true;
        }, 500);

      } else if (json.html.length === 0) {
        return json.html;
      } else {
        $post_content.after("<div id='end-results'><p>That's about it for <span>" + json.result + "</span>. Try another search?</p></div>")
      }
    }
  });
};

$(window).on('scroll', function() {
  if ($(window).scrollTop() + $(window).height() > $(document).height() / 1.25) {
    if (get_post_verify) {
      get_post_verify = false;
      visible_posts += 10;
      get_ten_posts(visible_posts);
    }
  }
});