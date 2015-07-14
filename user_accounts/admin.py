from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from user_accounts.models import User
from user_accounts.forms import UserChangeForm, RegistrationForm

class UserAccountAdmin(UserAdmin):
	form = UserChangeForm
	add_form = RegistrationForm

	list_display =('email', 'is_admin')
	list_filter = ('is_admin',)
	fieldsets = (
		(None, {'fields': ('email', 'password')}),
		('Permissions', {'fields': ('is_admin',)}),
	)

	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('email', 'password')}
		),
	)
	search_fields = ('email',)
	ordering = ('email',)
	filter_horizontal = ()

admin.site.register(User, UserAccountAdmin)
admin.site.unregister(Group)
