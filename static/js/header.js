var search_img, search_form, search_input,
		dashboard_body, explore_body, messages_body, dashboard, explore, messages,
		activity, account_a, account_details, account_list, account_list_li, account_list_p, 
		post, post_options, post_type, post_types, post_titles, title, 
		text, photo, quote, link, chat, audio, video,
		post_text, post_photo, post_quote, post_link, post_chat, post_audio, post_video,
		close_post, post_selection, title_field;

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

window.onload = function() {

	if (dashboard_body) {
		dashboard.style.backgroundImage = "url('/static/images/home_active.png')";
	}
	else if (explore_body) {
		explore.style.backgroundImage = "url('/static/images/explore_active.png')";
	}
	else if (messages_body) {
		messages.style.backgroundImage = "url('/static/images/messages_active.png)";
	}
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
account_list = document.getElementById("account-list");
account_list_li = account_list.querySelector("li");
account_list_p = account_list.querySelector("p");

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
		}, 20)
	}
}

var post_type_wrapper = document.getElementById("post-type-wrapper");

post.onclick = function(e) {
	e.preventDefault();

	/*post option appear animation(s)*/
	if (post_options.className === "post-fade post-hidden display-none") {
		post_type_wrapper.className = "";
		post_options.className = "post-fade post-hidden";

		setTimeout (function() {
			post_options.className = "post-fade visible";
		}, 1)

		setTimeout (function() {
			text.className = "type-anim type-visible";
			title[0].className = "p-fade p-visible";
		}, 10)

		setTimeout (function() {
			photo.className = "type-anim type-visible";
			title[1].className = "p-fade p-visible";
		}, 60)

		setTimeout (function() {
			quote.className = "type-anim type-visible";
			title[2].className = "p-fade p-visible";
		}, 110)

		setTimeout (function() {
			link.className = "type-anim type-visible";
			title[3].className = "p-fade p-visible";
		}, 160)

		setTimeout (function() {
			chat.className = "type-anim type-visible";
			title[4].className = "p-fade p-visible";
		}, 180)

		setTimeout (function() {
			audio.className = "type-anim type-visible";
			title[5].className = "p-fade p-visible";
		}, 230)

		setTimeout (function() {
			video.className = "type-anim type-visible";
			title[6].className = "p-fade p-visible";
		}, 280)
	}
}


document.onclick = function(e) {

	if (account_details.className === "account-fade account-visible") {

		if (e.target === account_details || e.target === account_list ||
			e.target === account_list_li || e.target === account_list_p) {
				return false;
		}
		else {
			account_details.className = "account-fade account-hidden";
			account_a.style.backgroundImage = null;

			setTimeout (function() {
				account_details.className = "account-fade account-hidden display-none";
			}, 100)
		}
	}
	else if (post_options.className === "post-fade visible") {

		/*post options disappear animation(s)*/
		if (e.target === post_type_wrapper) {
			link.className = "slide-up margin-top";
			title[3].className = "slide-up margin-top";

			setTimeout (function() {
				quote.className = "slide-up margin-top";
				chat.className = "slide-up margin-top";
				title[2].className = "slide-up margin-top";
				title[4].className = "slide-up margin-top";
			}, 50)

			setTimeout (function() {
				photo.className = "slide-up margin-top";
				audio.className = "slide-up margin-top";
				title[1].className = "slide-up margin-top";
				title[5].className = "slide-up margin-top";
			}, 100)

			setTimeout (function() {
				text.className = "slide-up margin-top";
				video.className = "slide-up margin-top";
				title[0].className = "slide-up margin-top";
				title[6].className = "slide-up margin-top";
			}, 150)

			setTimeout (function() {
				post_options.className = "post-fade post-hidden display-none";
			}, 250)

			/*This resets the divs and their corresponding p tags' classes
			to prepare them for the beginning animation cycle.*/
			setTimeout (function() {
				for (var i = 0; i < 7; i++) {
					post_types[i].className = "type-anim type-hidden";
					title[i].className = "p-fade p-hidden";
				}
			}, 300)
		}
	}
	// else if ()
}

close_post = document.querySelectorAll('.close-post');
submit_input = document.querySelectorAll('.submit-input');
post_submit_button = document.querySelectorAll('.submit-button');
post_selection = document.querySelectorAll(".post-selection");
title_field = document.querySelectorAll(".title-field");

function check_textarea() {
	for (var i = 0; i < title_field.length; i++) {
		title_field[i].style.height = 46 + 'px';
		var title_height = title_field[i].scrollHeight;
		title_field[i].style.height = title_height + 'px'; 
	}
}

for (var i = 0; i < title_field.length; i++) {
	title_field[i].addEventListener("keyup", check_textarea);
	title_field[i].addEventListener("keydown", check_textarea);
}

for (var i = 0; i < 7; i++) {

	(function() {
		var j = i;

		title[j].addEventListener("mouseover", function() {
			post_types[j].className = "type-anim hover";
		});

		title[j].addEventListener("mouseout", function() {
			post_types[j].className = "type-anim";
		});

		title[j].addEventListener("click", function() {
			post_types[j].click();
		});

		post_types[j].addEventListener("click", function() {
			post_type_wrapper.className = "display-none";
			document.body.style.cssText = "overflow: hidden;";
			post_selection[j].className = "post-selection display-table post-hidden";

			setTimeout (function() {
				post_selection[j].className = "post-selection display-table post-fade visible";
			},100)

			for (var i = 0; i < 7; i++) {
				post_types[i].className = "type-anim type-hidden";
				title[i].className = "p-fade p-hidden";
			}
		});

		close_post[j].addEventListener("click", function() {
			post_selection[j].className = "post-selection display-table post-fade post-hidden";

			setTimeout (function() {
				post_options.className = "post-fade post-hidden display-none";
				document.body.style.cssText = "";
				post_selection[j].className = "post-selection display-none";
			}, 200)
		});

		post_submit_button[j].addEventListener("click", function() {
			submit_input[j].click();
		});

	}())
}