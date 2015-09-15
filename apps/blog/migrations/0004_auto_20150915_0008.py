# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150915_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follow',
            name='blog',
            field=models.OneToOneField(to='blog.Blog'),
        ),
        migrations.AlterField(
            model_name='like',
            name='post',
            field=models.OneToOneField(to='blog.Post'),
        ),
    ]
