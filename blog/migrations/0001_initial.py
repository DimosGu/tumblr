# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import blog.models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=50, default='Untitled')),
                ('img', models.ImageField(upload_to=blog.models.upload_path, default='/media/default_blog_img.png')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('follow', models.ForeignKey(to='blog.Blog')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('pub_date', models.DateTimeField(verbose_name='date published', default=django.utils.timezone.now)),
                ('title', models.TextField(blank=True)),
                ('text', models.TextField(blank=True)),
                ('tags', models.TextField(blank=True)),
                ('file', models.FileField(upload_to=blog.models.upload_path, blank=True)),
                ('blog', models.ForeignKey(to='blog.Blog')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
