$(window).on('scroll', function() {
  if ($(window).scrollTop() + $(window).height() > $(document).height() / 1.25) {
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