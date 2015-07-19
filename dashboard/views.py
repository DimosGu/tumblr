from django.shortcuts import render
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
	return render(request, 'dashboard/dashboard.html')

def log_out(request):
	logout(request)
	return HttpResponseRedirect('/login')