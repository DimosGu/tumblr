from django import forms

class SearchForm(forms.Form):

  tags_search = forms.CharField(
    widget=forms.TextInput(attrs = {
      'id': 'search-input',
      'placeholder': 'Search Tumblr',
      'tabindex': '4',
    })
  )