from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from posts.forms import PostTextForm

@login_required
def dashboard(request):
	if request.method == 'POST':
		form = PostTextForm(request.POST)

	else:
		form = PostTextForm()

	return render(request, 'dashboard/dashboard.html', {'form': form})