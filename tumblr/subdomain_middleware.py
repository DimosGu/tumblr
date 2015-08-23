from django.http import HttpResponseRedirect
from sites.models import Site
from django.core.urlresolvers import reverse, resolve

class SubdomainMiddleware:
	def process_request(self, request):
		request.subdomain = None
		host = request.META.get('HTTP_HOST', '')
		hosts = host.split('.')

		if len(hosts) > 3:
			request.subdomain = ''.join(hosts[:-3])
			
			if request.get_full_path() != '/':
				return HttpResponseRedirect('http://%s%s' % ('.'.join(hosts[1:]), request.get_full_path()))
			else:

				try:
					user_domain = Site.objects.get(domain=request.subdomain)
				except: 
					user_domain = None
					return HttpResponseRedirect('http://%s' % '.'.join(hosts[1:]))