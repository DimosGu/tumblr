if (typeof get_post_verify === 'undefined') {
  get_post_verify = false;
}

function append_loading_anim(mini) {
  console.log(mini);
  animation_html = '<div id="loading-anim-container"><div class="loading-rect"></div>' +
  '<div class="loading-rect"></div><div class="loading-rect"></div></div>';

  if (mini) {
    $('#mini-posts-wrapper').append(animation_html);
  } else{
    $('#wrapper').append(animation_html);
  }
}

$(window).load(function() {
  var $no_post_div = $('#no-posts');

  if ($no_post_div.length) {
    get_post_verify = false;
  }

  if (typeof following_body === 'undefined' || following_body === null) {
    setTimeout (function() {
      if ($(document).height() === $(window).height() && get_post_verify) {
        get_ten_posts(visible_posts);
        get_post_verify = false;
        visible_posts += 10;
      }
    }, 1000)
  }
})

$(window).on('scroll', function() {
  if ((typeof following_body === 'undefined' || following_body === null) &&
    $(window).scrollTop() + $(window).height() > $(document).height() / 1.25) {

    if (get_post_verify) {
      get_post_verify = false;

      if (typeof site_username !== 'undefined') {
        get_ten_posts(visible_posts, site_username);
      } else {
        get_ten_posts(visible_posts);
      }
      visible_posts += 10;
      append_loading_anim();
    }
  }
});