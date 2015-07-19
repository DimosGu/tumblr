var search_img, search_form, search_input,
		activity, account_a, account_details, account_list, account_list_li, 
		account_list_p, post,
		post_titles, title, text, photo, quote, link,
		chat, audio, video;

search_img = new Image();
search_img.onload = function() {
}
search_img.src = '/static/images/white_search.png';

search_form = document.getElementById("search");
search_input = document.getElementById("search_input");

search_input.onfocus = function() {	
	search_form.className = "input_focus";

	if (search_input.value) {
		search_input.className = "visible";
	}
}

search_input.onblur = function() {
	search_form.className = "input_nofocus";
	
	if (search_input.value) {
		search_input.className = "fade";
	}
}	

activity = document.getElementById("activity");
post = document.getElementById("post");
post_options = document.getElementById("post_options");
post_type = document.getElementById("post_type");

account_a = document.getElementById('account_a');
account_details = document.getElementById("account_details");
account_list = document.getElementById("account_list");
account_list_li = account_list.querySelector("li");
account_list_p = account_list.querySelector("p");

post_titles = document.getElementById("post_titles");
title = post_titles.querySelectorAll("p");

text = document.getElementById("text");
photo = document.getElementById("photo");
quote = document.getElementById("quote");
link = document.getElementById("link");
chat = document.getElementById("chat");
audio = document.getElementById("audio");
video = document.getElementById("video");

activity.onclick = function() {
	event.preventDefault();
}

account_a.onclick = function() {
	event.preventDefault();

	if (account_details.className === "account_fade hidden display_none") {
		account_details.className = "account_fade hidden display_block";

		setTimeout (function() {
			account_details.className = "account_fade visible display_block";
		}, 1)
	}
}

post.onclick = function() {
	event.preventDefault();

	if (post_options.className === "post_fade post_hidden display_none") {
		post_options.className = "post_fade post_hidden display_block";

		setTimeout (function() {
			post_options.className = "post_fade post_visible display_block";
		}, 1)

		setTimeout (function() {
			text.className = "type_anim type_visible";
			title[0].className = "p_fade p_visible";
		}, 10)

		setTimeout (function() {
			photo.className = "type_anim type_visible";
			title[1].className = "p_fade p_visible";
		}, 60)

		setTimeout (function() {
			quote.className = "type_anim type_visible";
			title[2].className = "p_fade p_visible";
		}, 110)

		setTimeout (function() {
			link.className = "type_anim type_visible";
			title[3].className = "p_fade p_visible";
		}, 160)

		setTimeout (function() {
			chat.className = "type_anim type_visible";
			title[4].className = "p_fade p_visible";
		}, 180)

		setTimeout (function() {
			audio.className = "type_anim type_visible";
			title[5].className = "p_fade p_visible";
		}, 230)

		setTimeout (function() {
			video.className = "type_anim type_visible";
			title[6].className = "p_fade p_visible";
		}, 280)
	}
}

document.onclick = function(e) {

	if (account_details.className === "account_fade visible display_block") {

		if (e.target === account_details || e.target === account_list ||
			e.target === account_list_li || e.target === account_list_p) {
				return false;
		}
		else {
			account_details.className = "account_fade hidden display_block";

			setTimeout (function() {
				account_details.className = "account_fade hidden display_none";
			}, 100)
		}
	}

	else if (post_options.className === "post_fade post_visible display_block") {
		if (e.target === post_options) {
			link.className = "slide_up margin_top";
			title[3].className = "slide_up margin_top";

			setTimeout (function() {
				quote.className = "slide_up margin_top";
				chat.className = "slide_up margin_top";
				title[2].className = "slide_up margin_top";
				title[4].className = "slide_up margin_top";
			}, 100)

			setTimeout (function() {
				photo.className = "slide_up margin_top";
				audio.className = "slide_up margin_top";
				title[1].className = "slide_up margin_top";
				title[5].className = "slide_up margin_top";
			}, 200)

			setTimeout (function() {
				text.className = "slide_up margin_top";
				video.className = "slide_up margin_top";
				title[0].className = "slide_up margin_top";
				title[6].className = "slide_up margin_top";
			}, 300)

			setTimeout (function() {
				post_options.className = "post_fade post_hidden display_none";
			}, 400)

			setTimeout (function() {
				text.className = "type_anim type_hidden";
				photo.className = "type_anim type_hidden";
				quote.className = "type_anim type_hidden";
				link.className = "type_anim type_hidden";
				chat.className = "type_anim type_hidden";
				audio.className = "type_anim type_hidden";
				video.className = "type_anim type_hidden";
				title[0].className = "p_fade p_hidden";
				title[1].className = "p_fade p_hidden";
				title[2].className = "p_fade p_hidden";
				title[3].className = "p_fade p_hidden";
				title[4].className = "p_fade p_hidden";
				title[5].className = "p_fade p_hidden";
				title[6].className = "p_fade p_hidden";
			}, 500)
		}
		else {
			return false;
		}
	}
}

title[0].onmouseover = function() {
	text.className = "type_anim hover";
}
title[0].onmouseout = function() {
	text.className = "type_anim";
}

title[1].onmouseover = function() {
	photo.className = "type_anim hover";
}
title[1].onmouseout = function() {
	photo.className = "type_anim";
}

title[2].onmouseover = function() {
	quote.className = "type_anim hover";
}
title[2].onmouseout = function() {
	quote.className = "type_anim";
}

title[3].onmouseover = function() {
	link.className = "type_anim hover";
}
title[3].onmouseout = function() {
	link.className = "type_anim";
}

title[4].onmouseover = function() {
	chat.className = "type_anim hover";
}
title[4].onmouseout = function() {
	chat.className = "type_anim";
}

title[5].onmouseover = function() {
	audio.className = "type_anim hover";
}
title[5].onmouseout = function() {
	audio.className = "type_anim";
}

title[6].onmouseover = function() {
	video.className = "type_anim hover";
}
title[6].onmouseout = function() {
	video.className = "type_anim";
}


