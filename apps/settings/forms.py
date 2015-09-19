from django import forms
from apps.blog.models import Blog

class BlogEditForm(forms.ModelForm):

  header_img = forms.FileField(
    widget=forms.ClearableFileInput(attrs = {
      'id': 'header-img-input',
      'class': 'display-none',
      'accept': 'image/*',
    }),
  )

  avatar_img = forms.FileField(
    widget=forms.ClearableFileInput(attrs = {
      'id': 'avatar-img-input',
      'class': 'display-none',
      'accept': 'image/*',
    }),
  )

  class Meta:
    model = Blog
    fields = ('img', 'bg_img')