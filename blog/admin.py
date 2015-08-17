from django.contrib import admin

from .models import Blog, Post

class PostInline(admin.StackedInline):
	model = Post
	extra = 0

class BlogAdmin(admin.ModelAdmin):
	fields = ['title', 'user']
	inlines = [PostInline]

admin.site.register(Blog, BlogAdmin)

admin.site.register(Post)