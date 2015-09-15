# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone
import apps.blog.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='pub date')),
                ('title', models.CharField(max_length=50, default='Untitled')),
                ('img', models.ImageField(upload_to=apps.blog.models.upload_path, default='/media/default_blog_img.png')),
                ('bg_img', models.ImageField(upload_to=apps.blog.models.upload_path, default='/media/default_blog_bg.png')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='pub date')),
                ('blog', models.ForeignKey(to='blog.Blog')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='pub date')),
                ('title', models.TextField(blank=True)),
                ('text', models.TextField(blank=True)),
                ('file', models.FileField(upload_to=apps.blog.models.upload_path, blank=True)),
                ('notes', models.IntegerField(default=0)),
                ('blog', models.ForeignKey(to='blog.Blog')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
