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
  }, 100);
});

function get_ten_posts(post_count) {
  var $wrapper_data, $wrapper_sub_section, url;

  $wrapper_data = $('#wrapper').attr('data');
  $wrapper_sub_section = $('#wrapper').attr('data-sub-section');

  data = {
    'post_count': post_count,
  }

  if ($wrapper_data) {
    url = "/search/get_ten_posts"
    data['results'] = $wrapper_data;
  } else {
    url = "/explore/get_ten_posts";

    if ($wrapper_sub_section) {
      data['sub_section'] = $wrapper_sub_section;
    }
  }

  $.ajax({
    url: url,
    type: "GET",
    data: data,

    success: function(json) {

      if (typeof json.html != 'undefined' && json.html.length && json.html != "NoResults") {
        $explore_post_wrapper.append(json.html);
        $explore_post_wrapper.masonry('reloadItems');

        $explore_post_wrapper.imagesLoaded( function() {
          var $post_wrapper = $('.post-wrapper');

          $explore_post_wrapper.masonry('layout');
          $post_wrapper.removeClass('invisible');
          $('#loading-anim-container').remove();
          get_post_verify = true;
        });
      } else if ($wrapper_data && $wrapper_data != 'NoResults') {
        $('#loading-anim-container').remove();
        $explore_post_wrapper.after("<div id='end-results'><p>That's about it for <span>" + json.result + "</span>. Try another search?</p></div>")
      } else {
        $('#loading-anim-container').remove();
        return 'nothing';
      }
    }
  });
};