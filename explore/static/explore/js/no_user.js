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

register_body = document.getElementById("register-body");
login_body = document.getElementById("login-body");

email_signup = document.getElementById("email-signup");
email_login = document.getElementById("email-login");
account_form = document.getElementById("account-form");

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
}

h_logo = document.getElementById("h-logo");
sign_up_button = document.getElementById("sign-up");
login_button = document.getElementById("login");

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
