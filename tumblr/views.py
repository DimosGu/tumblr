from django.shortcuts import render

def error404(request):

  context = {}
  context['section'] = '404'
  context['page_title'] = 'Not found.'

  return render(request, '404.html', context)