var title_field, text_field, tags_field;

title_field = document.querySelectorAll(".title-field");
text_field = document.querySelectorAll(".text-field");
tags_field = document.querySelectorAll(".tags-field");

function check_title_field() {
  if (title_field[0].value != "" || text_field[0].value != "") {
    post_submit_button[0].className = "submit-button button-color";
  } else {
    post_submit_button[0].className = "submit-button";
  }

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
  } else {
    post_submit_button[0].className = "submit-button";
  }

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

function edit_post(type, id) {
  var $photo_data, text_data, data;

  $photo_data = new FormData($('#post-photo-form')[0]);
  $text_data = new FormData($('#post-text-form')[0]);

  if (type === 'photo') {
    $photo_data.append('post_edit_id', id);
    data = $photo_data;
  } else if (type === 'text') {
    $text_data.append('post_edit_id', id);
    data = $text_data;
  }

  $.ajax({
    url: "/blog/edit_post",
    type: "POST",
    data: data,
    processData: false,
    contentType: false,

    success: function(json) {
      var $update_this, $edit_post, $edit_title, $edit_text, $edit_tags, $edit_post_a, $edit_post_img,
          title_html, text_html, tags_html, tags_array, tags_join;

      if (blog_body) {
        $update_this = $('#blog-posts-wrapper').find('.post-wrapper[data-id="' + json.id_data + '"]');
        $edit_post = $update_this.children('.post');
        $words_wrapper = $edit_post.find('.words-wrapper');

        $edit_title = $edit_post.find('.post-title');
        $edit_text = $edit_post.find('.post-text');
        $edit_tags = $edit_post.find('.post-tags');

        title_html = '<span class="post-title">' + json.title_data + '</span>';
        text_html = '<p class="post-text">' + json.text_data + '</p>';

        tags_array = []
        for (var i = 0; i < json.tags_data.length; i++) {
          tags_array.push("<a title='" + json.tags_data[i] + "'href='http://" + json.domain_url + "/search/" + json.tags_data[i] + "'>#" + json.tags_data[i] + "</a>")
        }
        tags_join = tags_array.join('')
        tags_html = '<span class="post-tags">' + tags_join + '</span>';

        if (json.title_data) {
          if (json.title_data && $edit_title.length) {
            $edit_title.html(json.title_data);
          } else if (json.title_data && $edit_title.length == 0) {
            $words_wrapper.prepend(title_html);
          }
        } else if ($edit_title.length) {
          $edit_title.remove();

          //redefined for potential json.text_data if condition
          $edit_title = $words_wrapper.find('.post-tags');
        }

        $edit_post_a = $edit_post.children('a');
        $edit_post_img = $edit_post_a.children('img');

        if (json.file_data != $edit_post_img.attr('src')) {
          $edit_post_img.addClass('invisible');
          $edit_post_a.attr('href', json.file_data);
          $edit_post_img.attr('src', json.file_data);

          setTimeout (function() {
            if ($edit_post_img.width() <= 522) {
              $edit_post_img.css("margin-left", "18px");
            } else {
              $edit_post_img.css("margin-left", "0");
            }
            $edit_post_img.removeClass('invisible')
          }, 100);
        }

        if (json.text_data) {
          if (json.text_data && $edit_text.length) {
            $edit_text.html(json.text_data);
          } else if (json.text_data && json.file_data && $edit_text.length == 0) {
            $words_wrapper.prepend(text_html);
          } else if (json.text_data && json.file_data === undefined && $edit_text.length == 0 && $edit_title.length == 0) {
            $words_wrapper.prepend(text_html);
          } else if (json.text_data && $edit_text.length == 0 && $edit_title.length) {
            $edit_title.after(text_html);
          }
        } else if ($edit_text.length) {
          $edit_text.remove();
        }

        if (json.tags_data.length) {
          $edit_tags.remove();
          $words_wrapper.append(tags_html);
        } else {
          $edit_tags.remove();
        }
      }
    },
  });
};

function check_nopost_msg() {
  var $no_post_msg = $('#no-posts');

  if ($no_post_msg.length) {
    $no_post_msg.remove();
  }
}

function new_text_post() {

  $.ajax({
    url: "/blog/post_text",
    type: "POST",
    data: {
      title: title_field[0].value,
      text: text_field[0].value,
      tags: tags_field[0].value,
    },

    success: function(json) {
      var $post_wrapper = $('#blog-posts-wrapper');

      if (blog_body) {
        check_nopost_msg();
        $post_wrapper.prepend(json.html);
        visible_posts += 1;
      }
    },
  });
};

close_post[0].addEventListener('click', function() {
  setTimeout (function() {
    post_edit_id = null;
    title_field[0].value = "";
    text_field[0].value = "";
    tags_field[0].value = "";
    post_submit_button[0].className = 'submit-button';
    post_submit_button[0].innerHTML = "Post";
  }, 200);
});

$('#post-text-form').on('submit', function(event) {
  event.preventDefault();

  if (title_field[0].value != "" || text_field[0].value != "") {
    if (post_edit_id != null) {
      edit_post('text', post_edit_id);
    } else {
      new_text_post();
    }
    close_post[0].click();
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

img_hover_timer;

$('#img-preview, #erase-img').hover(
  function() {
    $('#erase-img').removeClass('display-none');

    if (img_hover_timer) {
      clearTimeout(img_hover_timer);
      img_hover_timer = null;
    }
  },
  function() {
    img_hover_timer = setTimeout (function() {
      $('#erase-img').addClass('display-none');
    }, 700);
  }
);

file_field = document.querySelectorAll(".file-field");

$('#erase-img').click(function() {
  $('#image-option').removeClass('display-none');
  $(this).addClass('display-none');
  file_field[0].value = "";
  $('#img-preview').attr('src', '').addClass('display-none');
  post_submit_button[1].className = "submit-button";
});

$photo_content = $('#post-photo').find(".post-content");

$("#photo-file").change(function(){
  $('#image-option').addClass("display-none");
  $photo_content.removeClass("display-none");
  photo_img_preview(this);
});


function new_photo_post() {
  var $data = new FormData($('#post-photo-form')[0]);

  $.ajax({
    url: "/blog/post_photo",
    type: "POST",
    data: $data,
    processData: false,
    contentType: false,

    success: function(json) {
      var $post_wrapper = $('#blog-posts-wrapper');

      if (blog_body) {
        check_nopost_msg();
        $post_wrapper.prepend(json.html);
        visible_posts += 1;
      }
    },
  });
};

close_post[1].addEventListener('click', function() {
  setTimeout (function() {
    file_field[0].value = "";
    text_field[1].value = "";
    tags_field[1].value = "";
    post_edit_id = null;
    $('#img-preview').attr('src', '');
    $('#image-option').removeClass("display-none");
    $photo_content.addClass("display-none");
    post_submit_button[1].className = "submit-button";
    post_submit_button[1].innerHTML = "Post";
  }, 200);
});

$('#post-photo-form').on('submit', function(event) {
  event.preventDefault();

  if ($('#img-preview').attr('src') != '') {
    if (post_edit_id != null) {
      edit_post('photo', post_edit_id);
    } else {
      new_photo_post();
    }
    close_post[1].click();
  }
});