from django.shortcuts import render
from django.contrib.auth import logout
from django.http import HttpResponseRedirect

def dashboard(request):
	return render(request, 'dashboard/index.html')

def log_out(request):
	logout(request)
	return HttpResponseRedirect('/login')