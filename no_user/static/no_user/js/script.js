var search_img, wrapper, center, header, email_input, account_form,
		form_errors, li_error,
		register_body, login_body, h_logo, sign_up_button, login_button,
		search_form, search_input;

search_img = new Image();
search_img.onload = function() {
}
search_img.src = '/static/images/white_search.png';

wrapper = document.getElementById("wrapper");
header = document.getElementById("header");
center = document.getElementById("center");

account_form = document.getElementById("account_form");
email_input = document.getElementById("id_email");

//These 2 error variables are login page exclusive.
form_errors = document.getElementById("form_errors");
li_error = form_errors.querySelector("li");

window.onload = function() {
	wrapper.className = "fade_in";
	email_input.focus();

	setTimeout (function() {
		header.className = "visible";
	}, 300)

	setTimeout (function() {
		center.className = "fade_in center_slide";		
	}, 900)

	if(li_error != null) {
		setTimeout (function() {
			form_errors.className = "error_slide error_visible"
		}, 1100)
	}
}

h_logo = document.getElementById("h_logo");
sign_up_button = document.getElementById("sign_up");
login_button = document.getElementById("login");

h_logo.onclick = function() {
	return false;
}

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