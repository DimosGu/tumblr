from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from blogs.forms import TextPostForm, PhotoPostForm
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

@login_required
def dashboard(request):
	return render(request, 'dashboard/dashboard.html') 