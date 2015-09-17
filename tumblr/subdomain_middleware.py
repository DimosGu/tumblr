from django.http import HttpResponseRedirect
from apps.user_accounts.models import User

class SubdomainMiddleware:
	def process_request(self, request):
		request.subdomain = None
		host = request.META['HTTP_HOST']
		hosts = host.split('.')

		if len(hosts) > 2 and hosts[0] != 'www' and hosts[0] != 'local':

			request.subdomain = hosts[0]
			path_info = request.META.get('PATH_INFO')
			dont_redirect = ['/', '/sites/get_ten_posts', '/following/follow', '/following/unfollow', '/likes/like', '/likes/unlike']

			if path_info in dont_redirect:

				try:
					user_domain = User.objects.get_by_username(request.subdomain)
				except:
					user_domain = None
					return HttpResponseRedirect('http://%s' % '.'.join(hosts[1:]))

			else:
				return HttpResponseRedirect('http://%s%s' % ('.'.join(hosts[1:]), path_info))
