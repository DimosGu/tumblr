from django import forms
from posts.models import PostText

class PostTextForm(forms.Form):

	title = forms.CharField(
		widget=forms.Textarea(attrs = {
			'rows': '1',
			'cols': '2',
			'class': 'title-field',
			'placeholder': 'Title',
		}),
	)

	text = forms.CharField(
		widget=forms.Textarea(attrs = {
			'class': 'text-field',
			'placeholder': 'Your text here',
		}),
	)

	tags = forms.CharField(
		widget=forms.Textarea(attrs = {
			'class': 'tags-field',
			'placeholder': '#tags',
		}),
	)

	class Meta:
		model = PostText

		fields = ('title', 'text', 'tags')