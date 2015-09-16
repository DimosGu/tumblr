var dashboard_body, explore_body, messages_body, likes_body, dashboard, explore, messages,
    $wrappepr, activity, account_a, account_details,
    post, post_options, post_type, post_types, post_titles, title,
    text, photo, quote, link, chat, audio, video, post_type_wrapper,
    post_text, post_photo, post_quote, post_link, post_chat, post_audio, post_video,
    close_post, post_selection,
    img_hover_timer, $photo_content, file_field;

dashboard = document.getElementById("dashboard");
explore = document.getElementById("explore");
messages = document.getElementById("messages");

dashboard_body = document.getElementById("dashboard-body");
explore_body = document.getElementById("explore-body");
messages_body = document.getElementById("messages-body");
blog_body = document.getElementById("blog-body");
likes_body = document.getElementById('likes-body');
following_body = document.getElementById('following-body');

$wrapper = $('#wrapper');
post_edit_id = null;
explore_body_attr = $('body').attr('data');

window.onload = function() {
  if (dashboard_body) {
    dashboard.style.backgroundImage = "url('/static/images/home_active.png')";
  } else if (explore_body && explore_body_attr == undefined) {
    explore.style.backgroundImage = "url('/static/images/explore_active.png')";
  } else if (messages_body) {
    messages.style.backgroundImage = "url('/static/images/messages_active.png)";
  } else if (blog_body || likes_body || following_body) {
    account_a.style.backgroundImage = "url('/static/images/account_active.png')";
  }

  setTimeout (function() {
    $wrapper.removeClass('display-none');
  }, 1);
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

messages.onclick = function(e) {
  e.preventDefault();
}

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
  post_type_wrapper.className = "";
  post_options.className = "post-fade invisible";

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

$(document).on('click', function (e) {

  if (account_details.className === "account-fade account-visible") {

    if (e.target === account_details || $(e.target).parents("#account-details").length) {
      return e.target
    } else {
      account_details.className = "account-fade account-hidden";

      if (blog_body === null) {
        account_a.style.backgroundImage = "";
      }

      setTimeout (function() {
        account_details.className = "account-fade account-hidden display-none";
      }, 100);
    }
  } else if (post_options.className === "post-fade visible") {

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
        post_options.className = "post-fade invisible display-none";
      }, 250);

      /*Resets the divs and their corresponding p tags' classes
      to prepare them for the beginning animation cycle.*/
      setTimeout (function() {
        for (var i = 0; i < 7; i++) {
          post_types[i].className = "type-hidden";
          title[i].className = "p-hidden";
        }
      }, 300);
    }
  }
})

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
        post_selection[j].className = "post-selection display-table invisible";

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
      post_selection[j].className = "post-selection display-table post-fade invisible";

      setTimeout (function() {
        post_options.className = "post-fade invisible display-none";
        document.body.style.cssText = "";
        post_selection[j].className = "post-selection display-none";
      }, 200);
    });

    post_submit_button[j].addEventListener("click", function() {
      submit_input[j].click();
    });

  }())
}