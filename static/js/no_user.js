var wrapper, center, header, email_input, account_form,
		form_errors, li_error,
		register_body, login_body, h_logo, sign_up_button, login_button;

wrapper = document.getElementById("wrapper");
header = document.getElementById("no-user-header");
center = document.getElementById("center");

register_body = document.getElementById("register-body");
login_body = document.getElementById("login-body");

email_signup = document.getElementById("email-signup");
email_login = document.getElementById("email-login");
account_form = document.getElementById("account-form");

//These 2 error variables are login page exclusive.
form_errors = document.getElementById("form-errors");
li_error = form_errors.querySelector("li");

window.onload = function() {
	wrapper.className = "fade-in";

	if (register_body) {
		email_signup.focus();
		sign_up_button.onclick = function() {
			return false;
		}
	} else if (login_body) {
		email_login.focus();
		login_button.onclick =function() {
			return false;
		}
	}

	setTimeout (function() {
		header.className = "visible";
	}, 300)

	setTimeout (function() {
		center.className = "fade-in center-slide";
	}, 900)

	if (li_error != null) {
		setTimeout (function() {
			form_errors.className = "error-slide error-visible"
		}, 1100)
	}
}

h_logo = document.getElementById("h-logo");
sign_up_button = document.getElementById("sign-up");
login_button = document.getElementById("login");

h_logo.onclick = function() {
	return false;
}