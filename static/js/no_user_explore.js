var search_img, $wrapper, header, search_form, search_input;

search_img = new Image();
search_img.onload = function() {
}
search_img.src = '/static/images/white_search.png';

$wrapper = $('#wrapper');
$wrapper.removeClass('display-none');

header = document.getElementById('no-user-header');
header.className = '';

search_form = document.getElementById("search");
search_input = document.getElementById("search-input");

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
