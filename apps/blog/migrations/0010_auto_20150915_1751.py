# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20150915_0350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='follow',
            name='blog',
        ),
        migrations.RemoveField(
            model_name='follow',
            name='user',
        ),
        migrations.RemoveField(
            model_name='like',
            name='post',
        ),
        migrations.RemoveField(
            model_name='like',
            name='user',
        ),
        migrations.DeleteModel(
            name='Follow',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
