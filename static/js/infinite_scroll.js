if (typeof get_post_verify === 'undefined') {
  get_post_verify = false;
}

$(window).load(function() {

  if (typeof following_body === 'undefined' || following_body === null) {
    setTimeout (function() {
      if ($(document).height() === $(window).height()) {
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
    }
  }
});