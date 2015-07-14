var search_img, search_form, search_input;

search_img = new Image();
search_img.onload = function() {
}
search_img.src = '/static/images/white_search.png';

search_form = document.getElementById("search");
search_input = document.getElementById("search_input");

search_input.onfocus = function() {	
	search_form.className = "input_focus";

	if(search_input.value) {
		search_input.className = "visible";
	}
}

search_input.onblur = function() {
	search_form.className = "input_nofocus";
	
	if(search_input.value) {
		search_input.className = "fade";
	}
}	