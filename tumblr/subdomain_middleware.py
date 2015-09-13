from django.http import HttpResponseRedirect
from apps.sites.models import Site

class SubdomainMiddleware:
	def process_request(self, request):
		request.subdomain = None
		host = request.META['HTTP_HOST']
		hosts = host.split('.')

		if len(hosts) > 2 and hosts[0] != 'www' and hosts[0] != 'local':

			# if hosts[1] == 'www':
			# 	hosts.pop(1)

			request.subdomain = hosts[0]
			path_info = request.META.get('PATH_INFO')
			dont_redirect = ['/', '/sites/get_ten_posts', '/blog/follow', '/blog/unfollow']

			if path_info in dont_redirect:

				try:
					user_domain = Site.objects.get_site_domain(request.subdomain)
				except:
					user_domain = None
					return HttpResponseRedirect('http://%s' % '.'.join(hosts[1:]))

			else:
				return HttpResponseRedirect('http://%s%s' % ('.'.join(hosts[1:]), path_info))
