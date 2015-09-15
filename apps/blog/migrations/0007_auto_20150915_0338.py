# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20150915_0334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follow',
            name='blog',
            field=models.ForeignKey(to='blog.Blog'),
        ),
        migrations.AlterField(
            model_name='like',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
