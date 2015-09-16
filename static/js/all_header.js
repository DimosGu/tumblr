var search_img, search_form, search_input, no_user_header, explore_body;

search_img = new Image();
search_img.onload = function() {
}
search_img.src = '/static/images/white_search.png';

search_form = document.getElementById("search");
search_input = document.getElementById("search-input");

no_user_header = document.getElementById('no-user-header');
explore_body = document.getElementById("explore-body");

if (no_user_header && explore_body) {
  var wrapper, header;

  no_user_header.className = '';

  window.onload = function() {
    wrapper = document.getElementById('wrapper');
    wrapper.className = '';
  }
}

search_input.onfocus = function() {
  search_form.className = "input-focus";

  if (search_input.value) {
    search_input.className = "visible";
  }
}

search_input.onblur = function() {
  search_form.className = "input-nofocus";

  if (search_input.value) {
    search_input.className = "fade";
  }
}