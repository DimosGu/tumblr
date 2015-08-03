from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from blogs.forms import TextPostForm, PhotoPostForm
from django.http import HttpResponse, HttpResponseRedirect

@login_required
def dashboard(request):
	text_form = TextPostForm()
	photo_form = PhotoPostForm()
	return render(request, 'dashboard/dashboard.html', 
		{'text_form': text_form, 'photo_form': photo_form}) 