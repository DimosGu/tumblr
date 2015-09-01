var form_error_id = $('#form-errors');

function check_field() {
	var email_val, password_val, username_val;

	email_val = $('#email-signup').val();
	password_val = $('#password-signup').val();
	username_val = $('#username-signup').val();

	$.ajax({
		url: "/check_fields",
		type: "POST",
		data: {
			email: email_val,
			password: password_val,
			username: username_val,
		},

		success: function(error) {
			if(error.email == "That's not a valid email address. Please try again.") {
				(form_error_id.html("<p>" + error.email + "</p>")
				.removeClass('error-invisible').addClass('error-visible'));
			}
			else if(error.password != undefined && password_val != "") {
				(form_error_id.html("<p>" + error.password + "</p>")
				.removeClass('error-invisible').addClass('error-visible'));
			}
			else if(error.username != undefined && username_val != "" &&
				error.username != 'Someone has already claimed the username') {
					(form_error_id.html("<p>" + error.username + "</p>")
					.removeClass('error-invisible').addClass('error-visible'));
			}
			else if(error.username == 'Someone has already claimed the username') {
				(form_error_id.html('<p>' + error.username + ' "' + username_val + '".</p>')
				.removeClass('error-invisible').addClass('error-visible'));
			}
			else if((error.email === undefined && password_val === "" && username_val === "") ||
				(error.password === undefined && email_val === "" && username_val === "") ||
				(error.username === undefined && email_val === "" && password_val === "") ||
				(error.email === undefined && error.password === undefined && username_val === "") ||
				(error.email === undefined && error.username === undefined && password_val === "") ||
				(error.password === undefined && error.username === undefined && email_val === "") ||
				(error.email === undefined && error.password === undefined &&
					error.username === undefined) ||
				(email_val === "" && password_val === "" && username_val === "")) {
					form_error_id.removeClass('error-visible').addClass('error-invisible');
			}
		},

		error: function() {
			form_error_id.html('<p>There was a form error.</p>');
		}
	});
};

$('#email-signup, #password-signup, #username-signup').blur(function() {
	check_field();
});

function submit_form() {
	var email_val, password_val, username_val;

	email_val = $('#email-signup').val();
	password_val = $('#password-signup').val();
	username_val = $('#username-signup').val();

	$.ajax({
		url: "/",
		type: "POST",
		data: {
			email: email_val,
			password: password_val,
			username: username_val,
		},

		success: function(json) {
			if(json.url != undefined) {
				window.location.href = json.url;
			}
			else if(json.email != undefined) {
				(form_error_id.html("<p>" + json.email + "</p>")
				.removeClass('error-invisible').addClass('error-visible'));
			}
			else if(json.password != undefined) {
				(form_error_id.html("<p>" + json.password + "</p>")
				.removeClass('error-invisible').addClass('error-visible'));
			}
			else if(json.username != undefined &&
				json.username != 'Someone has already claimed the username') {
					(form_error_id.html("<p>" + json.username + "</p>")
					.removeClass('error-invisible').addClass('error-visible'));
			}
			else if(json.username == 'Someone has already claimed the username') {
				(form_error_id.html('<p>' + json.username + ' "' + username_val + '".</p>')
				.removeClass('error-invisible').addClass('error-visible'));
			}
			else {
				return false;
			}
		},

		error: function() {
			form_error_id.html('<p>There was an issue logging in.</p>');
		}
	});
};

$('#account-form').on('submit', function(event) {
	event.preventDefault();
	submit_form();
});

function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie != '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = jQuery.trim(cookies[i]);
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) == (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
  	}
  }
  return cookieValue;
}
var csrftoken = getCookie('csrftoken');

/*
The functions below will create a header with csrftoken
*/

function csrfSafeMethod(method) {
  // these HTTP methods do not require CSRF protection
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
function sameOrigin(url) {
  // test that a given url is a same-origin URL
  // url could be relative or scheme relative or absolute
  var host = document.location.host; // host + port
  var protocol = document.location.protocol;
  var sr_origin = '//' + host;
  var origin = protocol + sr_origin;
  // Allow absolute or scheme relative URLs to same origin
  return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
    (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
    // or any other URL that isn't scheme relative or absolute i.e relative.
    !(/^(\/\/|http:|https:).*/.test(url));
}

$.ajaxSetup({
  beforeSend: function(xhr, settings) {
    if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
        // Send the token to same-origin, relative URLs only.
        // Send the token only if the method warrants CSRF protection
        // Using the CSRFToken value acquired earlier
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
  }
});