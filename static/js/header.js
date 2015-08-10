var search_img, search_form, search_input,
		dashboard_body, explore_body, messages_body, dashboard, explore, messages,
		activity, account_a, account_details, 
		post, post_options, post_type, post_types, post_titles, title, 
		text, photo, quote, link, chat, audio, video, post_type_wrapper,
		post_text, post_photo, post_quote, post_link, post_chat, post_audio, post_video,
		close_post, post_selection, title_field, text_field, tags_field;

search_img = new Image();
search_img.onload = function() {
}
search_img.src = '/static/images/white_search.png';

dashboard_body = document.getElementById("dashboard-body");
dashboard = document.getElementById("dashboard");
explore_body = document.getElementById("explore-body");
explore = document.getElementById("explore");
messages_body = document.getElementById("messages-body");
messages = document.getElementById("messages");
blog_body = document.getElementById("blog-body");

var wrapper = document.getElementById("wrapper");

// Timeouts to remove display-none class giving the page time to change 
// the image before displaying content
window.onload = function() {
	if (dashboard_body) {
		dashboard.style.backgroundImage = "url('/static/images/home_active.png')";
	} else if (explore_body) {
		explore.style.backgroundImage = "url('/static/images/explore_active.png')";
	} else if (messages_body) {
		messages.style.backgroundImage = "url('/static/images/messages_active.png)";
	} else if (blog_body) {
		blog_post_img = document.querySelectorAll('.blog-post-img');
		account_a.style.backgroundImage = "url('/static/images/account_active.png')";

		for (var i = 0; i < blog_post_img.length; i++) {
			if (blog_post_img[i].width <= 522) {
				blog_post_img[i].style.marginLeft = '18px';
			}
		}
	}

	setTimeout (function() {
		wrapper.className = "";
	}, 1);
}

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

activity = document.getElementById("activity");
account_a = document.getElementById('account-a');
account_details = document.getElementById("account-details");

post = document.getElementById("post");
post_options = document.getElementById("post-options");
post_type = document.getElementById("post-type");
post_types = post_type.querySelectorAll("div");
post_titles = document.getElementById("post-titles");
title = post_titles.querySelectorAll("p");

text = document.getElementById("text");
photo = document.getElementById("photo");
quote = document.getElementById("quote");
link = document.getElementById("link");
chat = document.getElementById("chat");
audio = document.getElementById("audio");
video = document.getElementById("video");

activity.onclick = function(e) {
	e.preventDefault();
}

account_a.onclick = function(e) {
	e.preventDefault();

	if (account_details.className === "account-fade account-hidden display-none") {
		account_details.className = "account-fade account-hidden";
		account_a.style.backgroundImage = "url('/static/images/account_active.png')";

		setTimeout (function() {
			account_details.className = "account-fade account-visible";
		}, 20);
	}
}

post_type_wrapper = document.getElementById("post-type-wrapper");

post.onclick = function(e) {
	e.preventDefault();

	/*post option appear animation(s)*/
	if (post_options.className === "post-fade post-hidden display-none") {
		post_type_wrapper.className = "";
		post_options.className = "post-fade post-hidden";

		setTimeout (function() {
			post_options.className = "post-fade visible";
		}, 1);

		setTimeout (function() {
			text.className = "type-anim type-visible";
			title[0].className = "p-fade p-visible";
		}, 10);

		setTimeout (function() {
			photo.className = "type-anim type-visible";
			title[1].className = "p-fade p-visible";
		}, 60);

		setTimeout (function() {
			quote.className = "type-anim type-visible";
			title[2].className = "p-fade p-visible";
		}, 110);

		setTimeout (function() {
			link.className = "type-anim type-visible";
			title[3].className = "p-fade p-visible";
		}, 160);

		setTimeout (function() {
			chat.className = "type-anim type-visible";
			title[4].className = "p-fade p-visible";
		}, 180);

		setTimeout (function() {
			audio.className = "type-anim type-visible";
			title[5].className = "p-fade p-visible";
		}, 230);

		setTimeout (function() {
			video.className = "type-anim type-visible";
			title[6].className = "p-fade p-visible";
		}, 280);
	}
}

document.onclick = function(e) {

	if (account_details.className === "account-fade account-visible") {

		if (e.target === account_details || $(e.target).parents("#account-details").length) {
			return e.target
		}	else {
			account_details.className = "account-fade account-hidden";

			if (blog_body === null) {
				account_a.style.backgroundImage = "";
			}

			setTimeout (function() {
				account_details.className = "account-fade account-hidden display-none";
			}, 100);
		}
	}	else if (post_options.className === "post-fade visible") {

		/*post options disappear animation(s)*/
		if (e.target === post_type_wrapper) {
			link.className = "slide-up margin-top";
			title[3].className = "slide-up margin-top";

			setTimeout (function() {
				quote.className = "slide-up margin-top";
				chat.className = "slide-up margin-top";
				title[2].className = "slide-up margin-top";
				title[4].className = "slide-up margin-top";
			}, 50);

			setTimeout (function() {
				photo.className = "slide-up margin-top";
				audio.className = "slide-up margin-top";
				title[1].className = "slide-up margin-top";
				title[5].className = "slide-up margin-top";
			}, 100);

			setTimeout (function() {
				text.className = "slide-up margin-top";
				video.className = "slide-up margin-top";
				title[0].className = "slide-up margin-top";
				title[6].className = "slide-up margin-top";
			}, 150);

			setTimeout (function() {
				post_options.className = "post-fade post-hidden display-none";
			}, 250);

			/*Resets the divs and their corresponding p tags' classes
			to prepare them for the beginning animation cycle.*/
			setTimeout (function() {
				for (var i = 0; i < 7; i++) {
					post_types[i].className = "type-anim type-hidden";
					title[i].className = "p-fade p-hidden";
				}
			}, 300);
		}
	}
}


close_post = document.querySelectorAll('.close-post');
submit_input = document.querySelectorAll('.submit-input');
post_submit_button = document.querySelectorAll('.submit-button');
post_selection = document.querySelectorAll(".post-selection");

//Event listeners/functions for the various posting divs/p/buttons.
for (var i = 0; i < 7; i++) {

	(function() {
		var j = i;

		function post_type_mouseover() {
			if (post_types[j].className != "slide-up margin-top") {
				post_types[j].className = "type-anim hover";
			}
		}

		function post_type_mouseout() {
			if (post_types[j].className != "slide-up margin-top") {
				post_types[j].className = "type-anim";
			}
		}

		function post_type_click() {
			if (post_types[j].className != "slide-up margin-top") {	
				post_type_wrapper.className = "display-none";
				document.body.style.cssText = "overflow: hidden;";
				post_selection[j].className = "post-selection display-table post-hidden";

				setTimeout (function() {
					post_selection[j].className = "post-selection display-table post-fade visible";
				}, 100);

				//Delay to resolve mouseout className change conflict
				setTimeout (function() {
					for (var i = 0; i < 7; i++) {
						post_types[i].className = "type-anim type-hidden";
						title[i].className = "p-fade p-hidden";	
					}
				}, 500);
			}
		}

		title[j].addEventListener("mouseover", post_type_mouseover)
		title[j].addEventListener("mouseout", post_type_mouseout) 
		title[j].addEventListener("click", post_type_click)

		post_types[j].addEventListener("mouseover", post_type_mouseover)
		post_types[j].addEventListener("mouseout", post_type_mouseout)
		post_types[j].addEventListener("click", post_type_click)

		close_post[j].addEventListener("click", function() {
			post_selection[j].className = "post-selection display-table post-fade post-hidden";

			setTimeout (function() {
				post_options.className = "post-fade post-hidden display-none";
				document.body.style.cssText = "";
				post_selection[j].className = "post-selection display-none";
			}, 200);
		});

		post_submit_button[j].addEventListener("click", function() {
			submit_input[j].click();
		});

	}())
}

title_field = document.querySelectorAll(".title-field");
text_field = document.querySelectorAll(".text-field");
tags_field = document.querySelectorAll(".tags-field");

function check_title_field() {
	if (title_field[0].value != "" || text_field[0].value != "") {
		post_submit_button[0].className = "submit-button button-color";
	} else {
		post_submit_button[0].className = "submit-button";
	}

	//This controls all title form field expansions in the header.
	for (var i = 0; i < title_field.length; i++) {
		title_field[i].style.height = 46 + 'px';
		var title_height = title_field[i].scrollHeight;
		title_field[i].style.height = title_height + 'px'; 
	}
}

for (var i = 0; i < title_field.length; i++) {
	title_field[i].addEventListener("keyup", check_title_field);
	title_field[i].addEventListener("keydown", check_title_field);
}

function check_text_field() {
	if (title_field[0].value != "" || text_field[0].value != "") {
		post_submit_button[0].className = "submit-button button-color";
	}	else {
		post_submit_button[0].className = "submit-button";
	}

	//This controls all tag form field expansions in the header.
	for (var i = 0; i < text_field.length; i++) {
		text_field[i].style.height = 63 + 'px';
		var text_height = text_field[i].scrollHeight;
		text_field[i].style.height = text_height + 'px';
	} 
}

for (var i = 0; i < text_field.length; i++) {
	text_field[i].addEventListener("keyup", check_text_field);
	text_field[i].addEventListener("keydown", check_text_field);
}

function check_tag_field() {
	
	//This controls all tags form field expansions in the header.
	for (var i = 0; i < tags_field.length; i++) {
		tags_field[i].style.height = 19 + 'px';
		var tags_height = tags_field[i].scrollHeight;
		tags_field[i].style.height = tags_height + 'px';
	}
}

for (var i = 0; i < tags_field.length; i++) {
	tags_field[i].addEventListener("keyup", check_tag_field);
	tags_field[i].addEventListener("keydown", check_tag_field);
}

//Posting forms
function submit_text_post() {
	$.ajax({
		url: "/blog/post_text",
		type: "POST",
		data: {
			title: title_field[0].value,
			text: text_field[0].value,
			tags: tags_field[0].value,
		}
	});
}

close_post[0].addEventListener('click', function() {
	setTimeout (function() {
		title_field[0].value = "";
		text_field[0].value = "";
		tags_field[0].value = "";
	}, 200);
});

$('#post-text-form').on('submit', function(event) {
	event.preventDefault();

	if (title_field[0].value != "" || text_field[0].value != "") {
		submit_text_post();
		close_post[0].click();

		if (blog_body) {

			setTimeout (function() {
				$('#blog-posts-wrapper').load(document.URL + ' #blog-posts-wrapper');
			}, 1000);
		}
	}
});

$('#upload-img').click(function() {
	$('#photo-file').click();
});

function photo_img_preview(input) {
	var img_preview = $("#img-preview");

  if (input.files && input.files[0]) {
    var reader = new FileReader();
    
    reader.onload = function (e) {
      img_preview.attr('src', e.target.result);
      img_preview.removeClass("display-none");
      post_submit_button[1].className = "submit-button button-color";
    }
    
    reader.readAsDataURL(input.files[0]);
  }
}

var photo_content = $('#post-photo').find(".post-content");

$("#photo-file").change(function(){
		$('#image-option').addClass("display-none");
		photo_content.removeClass("display-none");
    photo_img_preview(this);
});

var file_field = document.querySelectorAll(".file-field");

function submit_photo_post() {
	var data = new FormData($('#post-photo-form')[0]);

	$.ajax({
		url: "/blog/post_photo",
		type: "POST",
		data: data,
		processData: false,
		contentType: false
	});
}

close_post[1].addEventListener('click', function() {
	setTimeout (function() {
		file_field[0].value = "";
		text_field[1].value = "";
		tags_field[1].value = "";
		$('#img-preview').attr('src', '/');
		$('#image-option').removeClass("display-none");
		photo_content.addClass("display-none");
		post_submit_button[1].className = "submit-button";
	}, 200);
});

$('#post-photo-form').on('submit', function(event) {
	event.preventDefault();

	if (file_field[0].value != "") {
		submit_photo_post();
		close_post[1].click();

		if (blog_body) {
			setTimeout (function() {
				$('#blog-content').load(document.URL + ' #blog-posts-wrapper');
			}, 1000);
		}
	}
});

// This function gets cookie with a given name
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