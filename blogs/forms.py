from django import forms
from blogs.models import Post

class TextPostForm(forms.ModelForm):

	title = forms.CharField(required=False,
		widget=forms.Textarea(attrs = {
			'id': 'text-title-field',
			'class': 'title-field',
			'placeholder': 'Title',
		}),
	)

	text = forms.CharField(required=False,
		widget=forms.Textarea(attrs = {
			'id': 'text-text-field',
			'class': 'text-field',
			'placeholder': 'Your text here',
		}),
	)

	tags = forms.CharField(required=False,
		widget=forms.Textarea(attrs = {
			'class': 'tags-field',
			'placeholder': '#tags',
			'maxlength': '200',
		}),
	)

	class Meta:
		model = Post
		fields = ('title', 'text', 'tags')

class PhotoPostForm(forms.ModelForm):
	
	title = forms.CharField(required=False,
		widget=forms.Textarea(attrs = {
			'id': 'photo_title',
			'class': 'title-field',
			'placeholder': 'Title',
		}),
	)

	text = forms.CharField(required=False,
		widget=forms.Textarea(attrs = {
			'id': 'photo_text',
			'class': 'text-field',
			'placeholder': 'Your text here',
		}),
	)

	tags = forms.CharField(required=False,
		widget=forms.Textarea(attrs = {
			'id': 'photo_tags',
			'class': 'tags-field',
			'placeholder': '#tags',
			'maxlength': '200',
		}),
	)

	class Meta:
		model = Post
		fields = ('title', 'text', 'tags')